import asyncio
import logging
import signal
import sys
import traceback

from pipecat.frames.frames import EndFrame, InputAudioRawFrame
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask

from src.config import AgentConfig
from src.pipeline.agent_pipeline import TelephonyAgentPipeline
from .config import AUDIO_CHANNELS, AUDIO_SAMPLE_RATE, ROOM_ID
from .janus_orchestrator import JanusOrchestrator
from .media_bridge import MediaBridge, PipecatTTSAudioTrack
from .rtc_transport import RTCTransport

logger = logging.getLogger(__name__)


class JanusTransportManager:
    def __init__(self, config: AgentConfig) -> None:
        self.config = config

        self.media_bridge = MediaBridge(
            sample_rate=self.config.sample_rate,
            channels=AUDIO_CHANNELS,
        )
        self.rtc = RTCTransport(media_bridge=self.media_bridge)

        self.orchestrator = JanusOrchestrator()
        self.orchestrator.sip_bridge.set_incoming_offer_handler(self._handle_incoming_sip_offer)
        self.orchestrator.room_controller.set_callbacks(
            on_pipecat_connect=self.connect_pipecat,
            on_pipecat_disconnect=self.disconnect_pipecat,
        )

        self._pipeline_task = None
        self._runner_task = None
        self._feed_task = None

        self._stop_event = asyncio.Event()
        self._state_lock = asyncio.Lock()
        self._call_active = False
        self._media_frames_seen = 0

    async def start(self) -> None:
        await self.orchestrator.start()
        logger.info("[IDLE] waiting for caller in room %s", ROOM_ID)
        await self.wait_for_shutdown()

    async def stop(self) -> None:
        self._stop_event.set()
        await self.disconnect_pipecat()
        await self.orchestrator.stop()

    async def wait_for_shutdown(self) -> None:
        await self._stop_event.wait()

    async def connect_pipecat(self) -> None:
        async with self._state_lock:
            if self._call_active:
                return

            logger.info("[CONNECTING] joining Janus room")
            self.rtc.initialize()
            outbound_track = PipecatTTSAudioTrack(self.media_bridge)
            self.rtc.add_track(outbound_track)

            # Pipecat joins AudioBridge only when SIP call is active.
            await self.orchestrator.audiobridge.join_room(display="pipecat-voiceagent")
            self._call_active = True

            await self._start_pipeline()
            logger.info("[CONNECTED] media active")

    async def _handle_incoming_sip_offer(self, call_id: str | None, jsep: dict, raw_message: dict) -> None:
        """Handle incoming SIP JSEP offer, generate answer, and accept call."""
        import traceback
        try:
            print("[CALL] incomingcall START")
            async with self._state_lock:
                logger.warning("[WEBRTC] incoming SIP offer received call_id=%s", call_id)
                try:
                    logger.warning("[WEBRTC] creating/initializing RTCPeerConnection")
                    print("[WEBRTC] create pc START")
                    self.rtc.initialize()
                    print("[WEBRTC] create pc DONE")
                    logger.warning("[WEBRTC] RTCPeerConnection initialized")

                    logger.warning("[WEBRTC] adding outbound audio track")
                    outbound_track = PipecatTTSAudioTrack(self.media_bridge)
                    self.rtc.add_track(outbound_track)
                    logger.warning("[WEBRTC] outbound audio track added")

                    offer_sdp = jsep.get("sdp")
                    if not offer_sdp:
                        logger.error("[WEBRTC] missing SDP offer call_id=%s", call_id)
                        return

                    logger.warning("[WEBRTC] REMOTE SDP OFFER START")
                    print("[WEBRTC] REMOTE SDP START")
                    print(offer_sdp)
                    print("[WEBRTC] REMOTE SDP END")
                    logger.warning("%s", offer_sdp)
                    logger.warning("[WEBRTC] REMOTE SDP OFFER END")

                    answer_jsep = await self.rtc.create_audio_only_answer_for_offer(offer_sdp)
                    logger.warning("[WEBRTC] SDP answer created call_id=%s", call_id)

                    sip_handle = self.orchestrator.sip_bridge.handle_id
                    if not sip_handle:
                        logger.error("[WEBRTC] SIP handle missing call_id=%s", call_id)
                        return

                    body = {"request": "accept"}
                    logger.warning("[WEBRTC] sending SIP accept call_id=%s", call_id)
                    print("[WEBRTC] sending SIP accept")
                    response = await self.orchestrator.send_plugin_message(
                        sip_handle,
                        body=body,
                        jsep=answer_jsep,
                    )
                    print("[WEBRTC] SIP accept sent")
                    logger.warning("[WEBRTC] SIP accept response call_id=%s response=%s", call_id, response)
                except Exception as exc:
                    logger.error("[WEBRTC] incoming offer handling failed call_id=%s error=%s", call_id, exc)
                    print(f"[CALL_ERROR] {exc}")
                    traceback.print_exc()

        except Exception as e:
            print(f"[CALL_ERROR] {e}")
            traceback.print_exc()

    async def disconnect_pipecat(self) -> None:
        async with self._state_lock:
            if not self._call_active and not self._pipeline_task:
                return

            logger.info("[DISCONNECTING] cleaning up transport")
            await self._stop_pipeline()

            try:
                await self.orchestrator.audiobridge.leave_room()
            except Exception as exc:
                logger.warning("AudioBridge leave failed: %s", exc)

            await self.media_bridge.stop()
            self._drain_queue(self.media_bridge.inbound_queue)
            self._drain_queue(self.media_bridge.outbound_queue)

            await self.rtc.close()
            self._call_active = False
            logger.info("[IDLE] waiting for caller in room %s", ROOM_ID)
            logger.info("[CLEANUP_COMPLETE] room=%s", ROOM_ID)

    async def _start_pipeline(self) -> None:
        pipeline = TelephonyAgentPipeline(config=self.config, media_bridge=self.media_bridge)
        task = PipelineTask(
            pipeline.build_pipeline(),
            params=PipelineParams(
                allow_interruptions=True,
                enable_metrics=True,
                enable_usage_metrics=True,
            ),
        )
        self._pipeline_task = task

        runner = PipelineRunner(handle_sigint=False)
        self._runner_task = asyncio.create_task(runner.run(task))
        self._feed_task = asyncio.create_task(self._feed_inbound_audio())
        logger.info("Pipeline runner started")

    async def _stop_pipeline(self) -> None:
        if self._pipeline_task:
            try:
                await self._pipeline_task.queue_frames([EndFrame()])
            except Exception:
                pass

        if self._feed_task:
            self._feed_task.cancel()
            try:
                await self._feed_task
            except asyncio.CancelledError:
                pass
            self._feed_task = None

        if self._runner_task:
            self._runner_task.cancel()
            try:
                await self._runner_task
            except asyncio.CancelledError:
                pass
            self._runner_task = None

        self._pipeline_task = None

    async def _feed_inbound_audio(self) -> None:
        while not self._stop_event.is_set():
            pcm = await self.media_bridge.inbound_queue.get()
            if not self._call_active or not self._pipeline_task:
                continue

            frame = InputAudioRawFrame(
                audio=pcm,
                num_channels=1,
                sample_rate=AUDIO_SAMPLE_RATE,
            )
            await self._pipeline_task.queue_frames([frame])
            self._media_frames_seen += 1
            if self._media_frames_seen % 50 == 0:
                logger.info("[MEDIA_FLOWING] inbound_frames=%s", self._media_frames_seen)

    @staticmethod
    def _drain_queue(queue: asyncio.Queue) -> None:
        while not queue.empty():
            try:
                queue.get_nowait()
            except asyncio.QueueEmpty:
                break


async def run_manager(config: AgentConfig) -> None:
    manager = JanusTransportManager(config)

    loop = asyncio.get_running_loop()

    def shutdown() -> None:
        logger.info("Shutdown signal received")
        manager._stop_event.set()

    try:
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, shutdown)
    except NotImplementedError:
        pass

    try:
        logger.info("Janus transport manager running")
        await manager.start()
    except Exception as exc:
        logger.error("Transport manager error: %s", exc, exc_info=True)
    finally:
        logger.info("Transport manager shutting down")
        await manager.stop()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    from src.config import get_config

    run_config = get_config()
    asyncio.run(run_manager(run_config))

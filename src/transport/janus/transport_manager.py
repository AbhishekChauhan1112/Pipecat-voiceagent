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

            logger.info("[CONNECTING] joining Janus AudioBridge room as WebRTC participant")
            self.rtc.initialize()

            # aiortc creates an offer, joins AudioBridge, does full WebRTC negotiation
            await self.orchestrator.audiobridge.join_room(
                display="pipecat-voiceagent",
                rtc=self.rtc,
            )
            self._call_active = True

            await self._start_pipeline()
            logger.info("[CONNECTED] media active")

    async def _handle_incoming_sip_offer(self, call_id: str | None, jsep: dict, raw_message: dict) -> None:
        """Accept the incoming SIP call. SDP is NOT consumed here.

        The SIP plugin is call-control only. The actual WebRTC peer is the
        AudioBridge — aiortc will join it in connect_pipecat via join_room(rtc=...).
        """
        print("[SIP] incomingcall received call_id=", call_id)
        offer_sdp = jsep.get("sdp", "")
        logger.warning("[SIP_OFFER_PREVIEW] call_id=%s sdp_start=%s", call_id, offer_sdp[:200])
        print("[SIP] offer SDP (signaling only, NOT consumed by AudioBridge PC):", offer_sdp[:200], "...")

        sip_handle = self.orchestrator.sip_bridge.handle_id
        if not sip_handle:
            logger.error("[SIP] handle missing — cannot accept call")
            print("[FATAL] sip_bridge.handle_id is None")
            return

        if not offer_sdp:
            logger.error("[SIP] missing SDP in incomingcall jsep call_id=%s", call_id)
            print("[FATAL] jsep has no sdp field")
            return

        try:
            # ── Step 1: generate a valid SDP answer via a temporary signaling PC ──
            # The SIP offer is consumed ONLY in a throw-away RTCPeerConnection.
            # self.pc (AudioBridge peer) is NEVER touched in this path.
            print("[AIORTC_CREATE_ANSWER] generating SDP answer from SIP offer")
            logger.warning("[AIORTC_CREATE_ANSWER] call_id=%s", call_id)
            answer_jsep = await self.rtc.generate_sip_answer(offer_sdp)

            # ── Step 2: defensive validation ──────────────────────────────────────
            if answer_jsep.get("type") != "answer":
                raise RuntimeError(
                    f"[SIP_ACCEPT] expected answer type, got: {answer_jsep.get('type')}"
                )
            logger.warning(
                "[AIORTC_LOCAL_DESCRIPTION_READY] type=%s sdp_start=%s",
                answer_jsep["type"],
                answer_jsep["sdp"][:300],
            )

            # ── Step 3: send SIP accept with aiortc-generated SDP answer ──────────
            print("[SIP_ACCEPT_WITH_ANSWER] sending accept with aiortc answer JSEP")
            logger.warning("[SIP_ACCEPT_WITH_ANSWER] call_id=%s sip_handle=%s", call_id, sip_handle)
            response = await self.orchestrator.send_plugin_message(
                sip_handle,
                body={"request": "accept"},
                jsep=answer_jsep,      # aiortc-generated answer, NOT the echoed offer
                fire_and_forget=True,
            )
            print("[SIP] accept sent with answer:", response)
            logger.warning("[SIP] accept fire_and_forget response=%s", response)
            print("[AUDIOBRIDGE_NEGOTIATION_START] SIP accepted; AudioBridge WebRTC begins in connect_pipecat")
            logger.warning("[AUDIOBRIDGE_NEGOTIATION_START] call_id=%s", call_id)

        except Exception as exc:
            logger.error("[SIP] accept failed: %s", exc)
            print("[FATAL_EXCEPTION]", exc)
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

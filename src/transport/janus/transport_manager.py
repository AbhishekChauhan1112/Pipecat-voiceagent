import asyncio
import logging
import signal
import sys

from pipecat.frames.frames import InputAudioRawFrame
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask

from src.config import AgentConfig
from src.pipeline.agent_pipeline import TelephonyAgentPipeline
from .config import AUDIO_CHANNELS, AUDIO_SAMPLE_RATE
from .janus_client import JanusClient
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
        self.client = JanusClient(self.rtc)
        self.pipeline = TelephonyAgentPipeline(config=self.config, media_bridge=self.media_bridge)

        self._pipeline_task = None
        self._runner_task = None
        self._feed_task = None
        self._stop_event = asyncio.Event()

    async def start(self) -> None:
        await self._start_pipeline()
        await self._start_janus()

    async def stop(self) -> None:
        self._stop_event.set()
        if self._feed_task:
            self._feed_task.cancel()
        if self._runner_task:
            self._runner_task.cancel()
        await self.media_bridge.stop()
        await self.client.close()
        await self.rtc.close()

    async def wait_for_shutdown(self) -> None:
        await self._stop_event.wait()

    async def _start_pipeline(self) -> None:
        pipeline = self.pipeline.build_pipeline()
        task = PipelineTask(
            pipeline,
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

    async def _start_janus(self) -> None:
        await self.client.connect()
        await self.client.create_session()
        await self.client.attach_plugin()

        outbound_track = PipecatTTSAudioTrack(self.media_bridge)
        self.rtc.add_track(outbound_track)

        await self.client.join_room()
        await self.client.configure_webrtc()
        logger.info("Janus AudioBridge connected")

    async def _feed_inbound_audio(self) -> None:
        while not self._stop_event.is_set():
            pcm = await self.media_bridge.inbound_queue.get()
            frame = InputAudioRawFrame(
                audio=pcm,
                num_channels=1,
                sample_rate=AUDIO_SAMPLE_RATE,
            )
            await self._pipeline_task.queue_frames([frame])


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
        # Windows does not support add_signal_handler
        pass

    try:
        await manager.start()
        logger.info("Janus transport manager running")
        await manager.wait_for_shutdown()
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

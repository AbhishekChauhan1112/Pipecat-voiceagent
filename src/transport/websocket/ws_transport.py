"""
WebSocket transport for mod_audio_stream (FreeSWITCH).

Protocol (from mod_audio_stream source):
  Inbound  — binary WebSocket frames: interleaved L16 PCM, stereo, 16 kHz
              left channel = caller's voice, right channel = FreeSWITCH leg
  Outbound — JSON text frames:
              {
                "type": "streamAudio",
                "data": {
                  "audioDataType": "raw",
                  "sampleRate": 16000,
                  "audioData": "<base64-encoded mono L16 PCM>"
                }
              }

FreeSWITCH calls:
  uuid_audio_stream <uuid> start ws://127.0.0.1:8765 stereo 16000

Audio path:
  FS stereo 16kHz → extract left channel (caller) → InputAudioRawFrame
  → Pipecat pipeline (VAD→STT→LLM→TTS) → MediaBridgeOutputProcessor
  → outbound_queue → base64 → streamAudio JSON → mod_audio_stream plays file
"""

import asyncio
import base64
import json
import logging
import signal

import numpy as np
import websockets
from websockets.server import WebSocketServerProtocol

from pipecat.frames.frames import EndFrame, InputAudioRawFrame
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask

from src.config import AgentConfig
from src.pipeline.agent_pipeline import TelephonyAgentPipeline
from src.transport.janus.media_bridge import MediaBridge

logger = logging.getLogger(__name__)

WS_HOST = "0.0.0.0"
WS_PORT = 8765

# Must match the sample-rate argument in pipecat.lua's uuid_audio_stream call
SAMPLE_RATE = 16000

# FreeSWITCH sends stereo (left=caller, right=FS-callee leg)
FS_CHANNELS = 2

# Pipeline and output audio are mono
PIPELINE_CHANNELS = 1


class WebSocketTransportManager:
    def __init__(self, config: AgentConfig) -> None:
        self.config = config
        self._stop_event = asyncio.Event()

    async def start(self) -> None:
        server = await websockets.serve(
            self._handle_connection,
            WS_HOST,
            WS_PORT,
            ping_interval=None,  # mod_audio_stream closes connection on WebSocket pings
        )
        logger.info("[WS] Listening on ws://%s:%d", WS_HOST, WS_PORT)
        await self._stop_event.wait()
        server.close()
        await server.wait_closed()
        logger.info("[WS] Server stopped")

    async def stop(self) -> None:
        self._stop_event.set()

    async def _handle_connection(self, ws: WebSocketServerProtocol) -> None:
        remote = ws.remote_address
        logger.info("[WS] Connected: %s", remote)

        media_bridge = MediaBridge(
            sample_rate=SAMPLE_RATE,
            channels=PIPELINE_CHANNELS,
        )
        pipeline = TelephonyAgentPipeline(config=self.config, media_bridge=media_bridge)
        task = PipelineTask(
            pipeline.build_pipeline(),
            params=PipelineParams(
                allow_interruptions=True,
                enable_metrics=True,
                enable_usage_metrics=True,
            ),
        )
        runner = PipelineRunner(handle_sigint=False)

        runner_task = asyncio.create_task(runner.run(task))
        feed_task = asyncio.create_task(self._receive_audio(ws, task))
        send_task = asyncio.create_task(self._send_audio(ws, media_bridge))

        try:
            _done, pending = await asyncio.wait(
                [runner_task, feed_task, send_task],
                return_when=asyncio.FIRST_COMPLETED,
            )
        finally:
            # Stop pipeline cleanly so ElevenLabs/Groq connections are released
            try:
                await task.queue_frames([EndFrame()])
            except Exception:
                pass

            for t in [runner_task, feed_task, send_task]:
                t.cancel()
                try:
                    await t
                except (asyncio.CancelledError, Exception):
                    pass

            await media_bridge.stop()
            logger.info("[WS] Disconnected: %s", remote)

    async def _receive_audio(
        self, ws: WebSocketServerProtocol, task: PipelineTask
    ) -> None:
        """Receive binary stereo PCM from FreeSWITCH, extract caller (left) channel."""
        msg_count = 0
        print("[WS_RX] _receive_audio loop started", flush=True)
        async for message in ws:
            msg_count += 1
            if msg_count <= 5 or msg_count % 200 == 0:
                print(
                    f"[WS_RX] msg #{msg_count} type={type(message).__name__} "
                    f"len={len(message)}",
                    flush=True,
                )
            if not isinstance(message, bytes):
                logger.debug("[WS_RX] text frame: %s", message[:120])
                continue

            pcm = _stereo_to_mono(message)
            if not pcm:
                continue

            frame = InputAudioRawFrame(
                audio=pcm,
                num_channels=PIPELINE_CHANNELS,
                sample_rate=SAMPLE_RATE,
            )
            await task.queue_frames([frame])
        print(f"[WS_RX] _receive_audio loop exited after {msg_count} messages", flush=True)

    async def _send_audio(
        self, ws: WebSocketServerProtocol, media_bridge: MediaBridge
    ) -> None:
        """Read TTS PCM from outbound queue and send as streamAudio JSON to mod_audio_stream."""
        while True:
            pcm = await media_bridge.outbound_queue.get()
            audio_b64 = base64.b64encode(pcm).decode("ascii")
            msg = json.dumps(
                {
                    "type": "streamAudio",
                    "data": {
                        "audioDataType": "raw",
                        "sampleRate": SAMPLE_RATE,
                        "audioData": audio_b64,
                    },
                }
            )
            try:
                await ws.send(msg)
                logger.debug("[WS_TX] streamAudio bytes=%d", len(pcm))
            except websockets.ConnectionClosed:
                logger.info("[WS_TX] connection closed while sending audio")
                break


def _stereo_to_mono(raw: bytes) -> bytes:
    """Extract the left (caller) channel from interleaved L16 stereo PCM.

    mod_audio_stream sends: [L0,L0, R0,R0, L1,L1, R1,R1, ...]
    where left = caller's voice, right = FreeSWITCH internal leg.
    Taking every other int16 sample gives us the left channel.
    """
    if len(raw) % 4 != 0:
        # Odd frame size — not clean stereo; fall back to treating as mono
        logger.warning("[WS_RX] unexpected frame size %d (not divisible by 4)", len(raw))
        return raw

    samples = np.frombuffer(raw, dtype="<i2")   # little-endian int16
    left = samples[::2]                          # every other sample = left channel
    return left.tobytes()


async def run_ws_manager(config: AgentConfig) -> None:
    manager = WebSocketTransportManager(config)

    loop = asyncio.get_running_loop()

    def _shutdown() -> None:
        logger.info("[WS] Shutdown signal received")
        manager._stop_event.set()

    try:
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, _shutdown)
    except NotImplementedError:
        # Windows does not support add_signal_handler; rely on KeyboardInterrupt
        pass

    logger.info("[WS] WebSocket transport manager starting")
    await manager.start()

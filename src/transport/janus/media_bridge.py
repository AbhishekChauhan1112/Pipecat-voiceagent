import asyncio
import logging
import time
from fractions import Fraction

import numpy as np
from aiortc import MediaStreamTrack
from av import AudioFrame
from scipy.signal import resample

from pipecat.frames.frames import AudioRawFrame, TTSAudioRawFrame
from pipecat.processors.frame_processor import FrameDirection, FrameProcessor

logger = logging.getLogger(__name__)


class MediaBridge:
    """Bridge PCM audio between aiortc tracks and Pipecat queues."""

    def __init__(
        self,
        *,
        sample_rate: int = 16000,
        channels: int = 1,
        frame_ms: int = 20,
        max_queue_size: int = 200,
    ) -> None:
        self.sample_rate = sample_rate
        self.channels = channels
        self.frame_ms = frame_ms
        self.samples_per_frame = int(sample_rate * frame_ms / 1000)
        self.frame_bytes = self.samples_per_frame * 2

        self.inbound_queue: asyncio.Queue[bytes] = asyncio.Queue(maxsize=max_queue_size)
        self.outbound_queue: asyncio.Queue[bytes] = asyncio.Queue(maxsize=max_queue_size)

        self._inbound_task = None
        self._inbound_frames = 0
        self._outbound_frames = 0
        self._last_log_time = time.monotonic()

    def start_inbound(self, track: MediaStreamTrack) -> None:
        if self._inbound_task:
            return
        self._inbound_task = asyncio.create_task(self._consume_inbound(track))
        logger.info("Media bridge inbound consumer started for track %s", track.id)

    async def stop(self) -> None:
        if self._inbound_task:
            self._inbound_task.cancel()
            try:
                await self._inbound_task
            except asyncio.CancelledError:
                pass
            self._inbound_task = None

    async def enqueue_outbound_audio(
        self, audio: bytes, sample_rate: int, num_channels: int
    ) -> None:
        pcm = self._normalize_pcm(audio, sample_rate, num_channels)
        await self._queue_put(self.outbound_queue, pcm, direction="outbound")

    async def _consume_inbound(self, track: MediaStreamTrack) -> None:
        try:
            while True:
                frame = await track.recv()
                pcm = self._audioframe_to_pcm(frame)
                await self._queue_put(self.inbound_queue, pcm, direction="inbound")
        except asyncio.CancelledError:
            logger.debug("Inbound media bridge task cancelled.")
        except Exception as exc:
            logger.error("Inbound media bridge error: %s", exc)

    async def _queue_put(self, queue: asyncio.Queue, pcm: bytes, *, direction: str) -> None:
        if queue.full():
            try:
                queue.get_nowait()
                logger.warning("%s PCM queue full, dropping oldest frame", direction)
            except asyncio.QueueEmpty:
                pass

        await queue.put(pcm)

        now = time.monotonic()
        if now - self._last_log_time > 5.0:
            self._last_log_time = now
            logger.debug(
                "PCM queue stats: inbound=%s outbound=%s",
                self.inbound_queue.qsize(),
                self.outbound_queue.qsize(),
            )

    def _audioframe_to_pcm(self, frame: AudioFrame) -> bytes:
        pcm = frame.to_ndarray()
        if pcm.ndim == 2:
            if pcm.shape[0] > 1:
                pcm = np.mean(pcm, axis=0)
            else:
                pcm = pcm[0]

        pcm = pcm.astype(np.int16)
        if frame.sample_rate != self.sample_rate:
            pcm = self._resample_pcm(pcm, frame.sample_rate, self.sample_rate)

        self._inbound_frames += 1
        return pcm.tobytes()

    def _normalize_pcm(self, audio: bytes, sample_rate: int, num_channels: int) -> bytes:
        pcm = np.frombuffer(audio, dtype=np.int16)
        if num_channels > 1:
            pcm = pcm.reshape(-1, num_channels)
            pcm = np.mean(pcm, axis=1).astype(np.int16)

        if sample_rate != self.sample_rate:
            pcm = self._resample_pcm(pcm, sample_rate, self.sample_rate)

        self._outbound_frames += 1
        return pcm.tobytes()

    def _resample_pcm(self, samples: np.ndarray, src_rate: int, dst_rate: int) -> np.ndarray:
        num_samples = int(len(samples) * dst_rate / src_rate)
        resampled = resample(samples, num_samples).astype(np.int16)
        logger.debug("Resampled audio %sHz -> %sHz (%s samples)", src_rate, dst_rate, num_samples)
        return resampled


class PipecatTTSAudioTrack(MediaStreamTrack):
    """MediaStreamTrack that streams Pipecat TTS PCM frames to Janus."""

    kind = "audio"

    def __init__(self, media_bridge: MediaBridge) -> None:
        super().__init__()
        self.media_bridge = media_bridge
        self.sample_rate = media_bridge.sample_rate
        self.samples_per_frame = media_bridge.samples_per_frame
        self.frame_bytes = media_bridge.frame_bytes
        self._buffer = bytearray()
        self._timestamp = 0
        self._start_time = None

    async def recv(self):
        if self._start_time is None:
            self._start_time = time.time()
        else:
            wait = self._start_time + (self._timestamp / self.sample_rate) - time.time()
            if wait > 0:
                await asyncio.sleep(wait)

        while len(self._buffer) < self.frame_bytes:
            chunk = await self.media_bridge.outbound_queue.get()
            self._buffer.extend(chunk)

        frame_bytes = self._buffer[: self.frame_bytes]
        del self._buffer[: self.frame_bytes]

        frame = AudioFrame(format="s16", layout="mono", samples=self.samples_per_frame)
        frame.sample_rate = self.sample_rate
        frame.planes[0].update(bytes(frame_bytes))
        frame.pts = self._timestamp
        frame.time_base = Fraction(1, self.sample_rate)
        self._timestamp += self.samples_per_frame
        return frame


class MediaBridgeOutputProcessor(FrameProcessor):
    """Consumes Pipecat TTS frames and enqueues them for RTP output."""

    def __init__(self, media_bridge: MediaBridge) -> None:
        super().__init__()
        self.media_bridge = media_bridge

    async def process_frame(self, frame, direction: FrameDirection) -> None:
        await super().process_frame(frame, direction)

        if isinstance(frame, TTSAudioRawFrame):
            await self.media_bridge.enqueue_outbound_audio(
                frame.audio,
                sample_rate=frame.sample_rate,
                num_channels=frame.num_channels,
            )
        elif isinstance(frame, AudioRawFrame):
            await self.media_bridge.enqueue_outbound_audio(
                frame.audio,
                sample_rate=frame.sample_rate,
                num_channels=frame.num_channels,
            )

        await self.push_frame(frame, direction)

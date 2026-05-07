"""
Voice Agent Pipeline — Telephony Edition (with extensive debug logging).

Data flow:
  Linphone → SIP → FreeSWITCH → mod_audio_stream WebSocket (binary PCM16)
      → FreeSwitchAudioSerializer → VAD → Groq Whisper STT
      → User Context Aggregator → Groq LLM → ElevenLabs TTS
      → Assistant Context Aggregator → transport.output() → FreeSWITCH → Linphone
"""

import time
import uuid
from typing import AsyncGenerator

from loguru import logger

from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.audio.vad.vad_analyzer import VADParams
from pipecat.frames.frames import (
    AudioRawFrame,
    CancelFrame,
    EndFrame,
    Frame,
    InputAudioRawFrame,
    InterimTranscriptionFrame,
    LLMMessagesUpdateFrame,
    MetricsFrame,
    StartInterruptionFrame,
    TextFrame,
    TranscriptionFrame,
    TTSAudioRawFrame,
    TTSStartedFrame,
    TTSStoppedFrame,
    UserStartedSpeakingFrame,
    UserStoppedSpeakingFrame,
)
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask
from pipecat.processors.audio.vad_processor import VADProcessor
from pipecat.processors.frame_processor import FrameDirection, FrameProcessor
from pipecat.transports.websocket.fastapi import (
    FastAPIWebsocketParams,
    FastAPIWebsocketTransport,
)
from fastapi import WebSocket

from src.config import AgentConfig
from src.logging_utils import LatencyTracker, get_session_logger
from src.services.llm_service import build_groq_llm
from src.services.groq_stt_service import build_groq_stt
from src.services.tts_service import build_elevenlabs_tts
from src.transport.freeswitch_serializer import FreeSwitchAudioSerializer


# ── Debug frame observer ───────────────────────────────────────────────────────

class DebugFrameLogger(FrameProcessor):
    """Sits at a named point in the pipeline and logs every frame passing through.

    Useful for confirming that audio, transcriptions, LLM tokens, and TTS
    audio are actually flowing through the pipeline end-to-end.
    """

    def __init__(self, label: str, session_id: str, *, log_audio: bool = False) -> None:
        super().__init__()
        self._label = label
        self._sid = session_id
        self._log_audio = log_audio
        self._frame_counts: dict[str, int] = {}
        self._audio_bytes_seen = 0
        self._last_report = time.monotonic()

    async def process_frame(self, frame: Frame, direction: FrameDirection) -> None:
        await super().process_frame(frame, direction)

        frame_type = type(frame).__name__
        self._frame_counts[frame_type] = self._frame_counts.get(frame_type, 0) + 1

        # Always log important semantic frames
        if isinstance(frame, TranscriptionFrame):
            logger.debug(
                f"[{self._label}] 📝 TRANSCRIPTION: '{frame.text}' "
                f"(user={frame.user_id})"
            )
        elif isinstance(frame, InterimTranscriptionFrame):
            logger.debug(
                f"[{self._label}] 📝 INTERIM: '{frame.text}'"
            )
        elif isinstance(frame, TextFrame):
            logger.debug(
                f"[{self._label}] 💬 LLM TOKEN: '{frame.text}'"
            )
        elif isinstance(frame, TTSStartedFrame):
            logger.info(f"[{self._label}] 🔊 TTS STARTED")
        elif isinstance(frame, TTSStoppedFrame):
            logger.info(f"[{self._label}] 🔇 TTS STOPPED")
        elif isinstance(frame, TTSAudioRawFrame):
            logger.debug(
                f"[{self._label}] 🎵 TTS AUDIO: {len(frame.audio)} bytes "
                f"rate={frame.sample_rate}"
            )
        elif isinstance(frame, UserStartedSpeakingFrame):
            logger.info(f"[{self._label}] 🎤 USER STARTED SPEAKING")
        elif isinstance(frame, UserStoppedSpeakingFrame):
            logger.info(f"[{self._label}] 🔕 USER STOPPED SPEAKING")
        elif isinstance(frame, StartInterruptionFrame):
            logger.warning(f"[{self._label}] ⚡ BARGE-IN / INTERRUPTION")
        elif isinstance(frame, CancelFrame):
            logger.warning(f"[{self._label}] ❌ CANCEL FRAME")
        elif isinstance(frame, EndFrame):
            logger.info(f"[{self._label}] 🏁 END FRAME — pipeline shutting down")
        elif isinstance(frame, MetricsFrame):
            logger.debug(f"[{self._label}] 📊 METRICS: {frame}")
        elif isinstance(frame, InputAudioRawFrame) and self._log_audio:
            self._audio_bytes_seen += len(frame.audio)
            now = time.monotonic()
            if now - self._last_report > 5.0:
                logger.debug(
                    f"[{self._label}] 🔉 AUDIO IN: {self._audio_bytes_seen} bytes "
                    f"total in last 5s, rate={frame.sample_rate}"
                )
                self._audio_bytes_seen = 0
                self._last_report = now
        elif isinstance(frame, AudioRawFrame) and self._log_audio:
            self._audio_bytes_seen += len(frame.audio)
            now = time.monotonic()
            if now - self._last_report > 5.0:
                logger.debug(
                    f"[{self._label}] 🔈 AUDIO OUT: {self._audio_bytes_seen} bytes "
                    f"total in last 5s"
                )
                self._audio_bytes_seen = 0
                self._last_report = now
        else:
            # Log all other frame types at trace level so they don't flood logs
            logger.trace(f"[{self._label}] frame={frame_type} dir={direction.name}")

        await self.push_frame(frame, direction)

    async def cleanup(self) -> None:
        logger.debug(
            f"[{self._label}] Frame count summary: "
            + ", ".join(f"{k}={v}" for k, v in sorted(self._frame_counts.items()))
        )


# ── Pipeline ───────────────────────────────────────────────────────────────────

class TelephonyAgentPipeline:
    """Manages one complete realtime voice pipeline for a single phone call."""

    def __init__(self, websocket: WebSocket, config: AgentConfig) -> None:
        self.websocket = websocket
        self.config = config
        self.session_id = str(uuid.uuid4())
        self._log = get_session_logger(self.session_id)
        self._latency = LatencyTracker(self.session_id)

    async def run(self) -> None:
        self._log.info("Call session started", session_id=self.session_id)
        self._latency.mark("call_start")
        try:
            await self._run_pipeline()
        except Exception as exc:
            self._log.exception("Pipeline error", error=str(exc))
            raise
        finally:
            self._latency.record("call_duration", "call_start")
            self._latency.log_summary()
            self._log.info("Call session ended", session_id=self.session_id)

    async def _run_pipeline(self) -> None:
        sid = self.session_id

        # ── Serializer ────────────────────────────────────────────────────────
        serializer = FreeSwitchAudioSerializer(sample_rate=self.config.sample_rate)
        logger.debug(f"[{sid}] Serializer ready — sample_rate={self.config.sample_rate}")

        # ── Transport ─────────────────────────────────────────────────────────
        transport = FastAPIWebsocketTransport(
            websocket=self.websocket,
            params=FastAPIWebsocketParams(
                audio_in_enabled=True,
                audio_out_enabled=True,
                add_wav_header=False,
                serializer=serializer,
            ),
        )
        logger.debug(f"[{sid}] Transport created")

        # ── VAD ───────────────────────────────────────────────────────────────
        vad = VADProcessor(
            vad_analyzer=SileroVADAnalyzer(
                params=VADParams(
                    confidence=0.7,
                    start_secs=0.2,
                    stop_secs=0.8,
                    min_volume=0.6,
                )
            )
        )
        logger.debug(f"[{sid}] VAD processor created (Silero, confidence=0.7)")

        # ── AI Services ───────────────────────────────────────────────────────
        logger.debug(f"[{sid}] Building AI services...")
        stt = build_groq_stt(self.config)
        logger.info(f"[{sid}] STT ready: Groq Whisper")

        llm, ctx = build_groq_llm(self.config)
        logger.info(f"[{sid}] LLM ready: {self.config.groq_model}")

        tts = build_elevenlabs_tts(self.config)
        logger.info(f"[{sid}] TTS ready: ElevenLabs {self.config.elevenlabs_model}")

        # ── Debug observers ───────────────────────────────────────────────────
        # Place probes between each stage to see exactly what's flowing where.
        dbg_after_transport = DebugFrameLogger("AFTER_TRANSPORT", sid, log_audio=True)
        dbg_after_vad       = DebugFrameLogger("AFTER_VAD",       sid, log_audio=False)
        dbg_after_stt       = DebugFrameLogger("AFTER_STT",       sid)
        dbg_after_llm       = DebugFrameLogger("AFTER_LLM",       sid)
        dbg_after_tts       = DebugFrameLogger("AFTER_TTS",       sid, log_audio=True)

        # ── Pipeline ──────────────────────────────────────────────────────────
        pipeline = Pipeline(
            [
                transport.input(),      # 1. raw PCM from FreeSWITCH
                dbg_after_transport,    #    ← debug: what enters the pipeline?
                vad,                    # 2. Silero VAD — speech detection
                dbg_after_vad,          #    ← debug: VAD events, speech start/stop
                stt,                    # 3. Groq Whisper STT
                dbg_after_stt,          #    ← debug: transcriptions
                ctx.user(),             # 4. accumulate turns → LLM context
                llm,                    # 5. Groq LLM
                dbg_after_llm,          #    ← debug: LLM token stream
                tts,                    # 6. ElevenLabs TTS
                ctx.assistant(),        # 7. store bot reply (passes audio through)
                dbg_after_tts,          #    ← debug: TTS audio reaching transport
                transport.output(),     # 8. raw PCM → FreeSWITCH → caller
            ]
        )
        logger.debug(f"[{sid}] Pipeline assembled with 8 stages + 5 debug observers")

        # ── Task ──────────────────────────────────────────────────────────────
        task = PipelineTask(
            pipeline,
            params=PipelineParams(
                allow_interruptions=True,
                enable_metrics=True,
                enable_usage_metrics=True,
            ),
        )

        # ── Event handlers ────────────────────────────────────────────────────
        @transport.event_handler("on_client_connected")
        async def on_connected(transport_obj, client):
            call_uuid = serializer.call_uuid or "pending"
            self._log.info(
                "FreeSWITCH connected",
                call_uuid=call_uuid,
                client=str(client),
            )
            self._latency.mark("client_connected")
            logger.debug(
                f"[{sid}] Sending greeting LLMMessagesUpdateFrame to pipeline"
            )
            await task.queue_frames(
                [
                    LLMMessagesUpdateFrame(
                        messages=[
                            {"role": "system", "content": self.config.system_prompt},
                            {"role": "user",   "content": "Hello, I just picked up the phone."},
                        ],
                        run_llm=True,
                    )
                ]
            )
            logger.debug(f"[{sid}] Greeting frame queued")

        @transport.event_handler("on_client_disconnected")
        async def on_disconnected(transport_obj, client):
            self._log.info(
                "FreeSWITCH disconnected",
                call_uuid=serializer.call_uuid or "unknown",
            )
            await task.cancel()

        # ── Run ───────────────────────────────────────────────────────────────
        runner = PipelineRunner(handle_sigint=False)
        self._log.info("Pipeline running — waiting for audio from FreeSWITCH")
        logger.debug(
            f"[{sid}] WebSocket transport audio_in={True} audio_out={True} "
            f"sample_rate={self.config.sample_rate}"
        )
        await runner.run(task)

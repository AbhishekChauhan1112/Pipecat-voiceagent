"""
Voice Agent Pipeline — Janus WebRTC Edition (with extensive debug logging).

Data flow:
    Linphone → SIP → FreeSWITCH → Janus AudioBridge → aiortc inbound track
            → MediaBridge → VAD → Groq Whisper STT
            → User Context Aggregator → Groq LLM → ElevenLabs TTS
            → Assistant Context Aggregator → MediaBridge output → Janus → FreeSWITCH
"""

import time
import uuid

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
    MetricsFrame,
    InterruptionFrame,
    TextFrame,
    TranscriptionFrame,
    TTSAudioRawFrame,
    TTSStartedFrame,
    TTSStoppedFrame,
    UserStartedSpeakingFrame,
    UserStoppedSpeakingFrame,
)
from pipecat.pipeline.pipeline import Pipeline
from pipecat.processors.audio.vad_processor import VADProcessor
from pipecat.processors.frame_processor import FrameDirection, FrameProcessor
from src.config import AgentConfig
from src.logging_utils import LatencyTracker, get_session_logger
from src.services.llm_service import build_groq_llm
from src.services.groq_stt_service import build_groq_stt
from src.services.tts_service import build_elevenlabs_tts
from src.transport.janus.media_bridge import MediaBridge, MediaBridgeOutputProcessor


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

        logger.info(
            f"[{self._label}] FRAME TYPE: {type(frame).__name__}"
        )

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
            logger.info(
                f"[{self._label}] 🎵 TTS AUDIO: {len(frame.audio)} bytes "
                f"rate={frame.sample_rate}"
            )
        elif isinstance(frame, UserStartedSpeakingFrame):
            logger.info(f"[{self._label}] 🎤 USER STARTED SPEAKING")
        elif isinstance(frame, UserStoppedSpeakingFrame):
            logger.info(f"[{self._label}] 🔕 USER STOPPED SPEAKING")
        elif isinstance(frame, InterruptionFrame):
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

    def __init__(self, config: AgentConfig, media_bridge: MediaBridge) -> None:
        self.config = config
        self.media_bridge = media_bridge
        self.session_id = str(uuid.uuid4())
        self._log = get_session_logger(self.session_id)
        self._latency = LatencyTracker(self.session_id)

    def build_pipeline(self) -> Pipeline:
        sid = self.session_id

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
        dbg_after_transport = DebugFrameLogger("AFTER_TRANSPORT", sid, log_audio=True)
        dbg_after_vad = DebugFrameLogger("AFTER_VAD", sid, log_audio=False)
        dbg_after_stt = DebugFrameLogger("AFTER_STT", sid)
        dbg_after_llm = DebugFrameLogger("AFTER_LLM", sid)
        dbg_after_tts = DebugFrameLogger("AFTER_TTS", sid, log_audio=True)

        output = MediaBridgeOutputProcessor(self.media_bridge)

        pipeline = Pipeline(
            [
                # 1. Inbound audio is injected directly into the pipeline
                dbg_after_transport,

                # 2. Voice Activity Detection
                vad,

                # Debug VAD behavior
                dbg_after_vad,

                # 3. Speech-to-Text
                stt,

                # Debug STT output
                dbg_after_stt,

                # 4. Add user utterances into conversation memory
                ctx.user(),

                # 5. Large Language Model
                llm,

                # Debug LLM streaming tokens
                dbg_after_llm,

                # 6. Store assistant responses BEFORE TTS/output
                ctx.assistant(),

                # 7. Text-to-Speech synthesis
                tts,

                # Debug synthesized audio frames
                dbg_after_tts,

                # 8. Enqueue audio back to Janus RTP output
                output,
            ]
        )
        logger.debug(f"[{sid}] Pipeline assembled with 8 stages + 5 debug observers")
        return pipeline

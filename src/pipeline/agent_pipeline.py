"""
Voice Agent Pipeline — Telephony Edition.

Assembles the Pipecat pipeline for a single inbound FreeSWITCH call.

Data flow
─────────
  Linphone → SIP → FreeSWITCH (ext 9000)
      → mod_audio_stream WebSocket (binary PCM16)
          → [FreeSwitchAudioSerializer]   deserialize raw bytes → InputAudioRawFrame
          → [Silero VAD]                  detect speech / silence
          → [Deepgram STT]               stream audio → TranscriptionFrame
          → [User Context Aggregator]     buffer turns → LLMMessagesFrame
          → [Groq LLM]                   stream tokens
          → [ElevenLabs TTS]             stream PCM16 audio chunks
          → [Assistant Context Agg.]      store bot reply in memory
          → [FreeSwitchAudioSerializer]   serialize AudioRawFrame → raw bytes
      → mod_audio_stream WebSocket (binary PCM16)
  FreeSWITCH → RTP → Linphone (caller hears the agent)

Interruption / barge-in
───────────────────────
If the caller speaks while the agent is talking:
  1. Silero VAD fires VADUserStartedSpeakingFrame
  2. Transport emits StartInterruptionFrame
  3. ElevenLabs TTS and Groq LLM receive CancelFrame → stop immediately
  4. No more audio is sent back to the caller
  5. A new STT → LLM → TTS cycle begins with what the caller said
"""

import uuid

from loguru import logger

from pipecat.audio.vad.silero import SileroVADAnalyzer
from pipecat.audio.vad.vad_analyzer import VADParams
from pipecat.frames.frames import LLMMessagesUpdateFrame
from pipecat.pipeline.pipeline import Pipeline
from pipecat.pipeline.runner import PipelineRunner
from pipecat.pipeline.task import PipelineParams, PipelineTask
from pipecat.processors.audio.vad_processor import VADProcessor
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


class TelephonyAgentPipeline:
    """Manages one complete realtime voice pipeline for a single phone call.

    One instance is created per incoming WebSocket connection from FreeSWITCH
    (i.e., per inbound call). Pipelines are fully isolated — multiple concurrent
    calls each get their own Pipecat pipeline, services, and conversation context.

    Lifecycle:
        pipeline = TelephonyAgentPipeline(websocket, config)
        await pipeline.run()   # blocks until call ends / WebSocket closes
    """

    def __init__(self, websocket: WebSocket, config: AgentConfig) -> None:
        self.websocket = websocket
        self.config = config
        self.session_id = str(uuid.uuid4())
        self._log = get_session_logger(self.session_id)
        self._latency = LatencyTracker(self.session_id)

    async def run(self) -> None:
        """Build the pipeline and run it until the call ends."""
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

        # ── Serializer ───────────────────────────────────────────────────────
        # Translates between raw binary PCM16 (FreeSWITCH wire format)
        # and Pipecat's AudioRawFrame objects.
        serializer = FreeSwitchAudioSerializer(sample_rate=self.config.sample_rate)

        # ── Transport ────────────────────────────────────────────────────────
        # FastAPIWebsocketTransport manages the WebSocket lifecycle and
        # converts binary PCM ↔ Pipecat frames using the serializer above.
        # Silero VAD runs inside the transport so barge-in detection happens
        # as close to the audio source as possible.
        transport = FastAPIWebsocketTransport(
            websocket=self.websocket,
            params=FastAPIWebsocketParams(
                audio_in_enabled=True,
                audio_out_enabled=True,
                add_wav_header=False,
                serializer=serializer,
            ),
        )

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

        # ── AI Services ──────────────────────────────────────────────────────
        stt = build_groq_stt(self.config)
        llm, ctx = build_groq_llm(self.config)
        tts = build_elevenlabs_tts(self.config)

        # ── Pipeline ─────────────────────────────────────────────────────────
        pipeline = Pipeline(
            [
                transport.input(),       # 1. raw PCM from FreeSWITCH
                vad,                     # 2. Silero VAD — barge-in / endpointing
                stt,                     # 3. Deepgram streaming STT
                ctx.user(),              # 4. accumulate turns → LLM context
                llm,                     # 5. Groq streaming LLM
                tts,                     # 6. ElevenLabs streaming TTS
                ctx.assistant(),         # 7. store bot reply in memory
                transport.output(),      # 8. raw PCM back to FreeSWITCH
            ]
        )

        # ── Task ─────────────────────────────────────────────────────────────
        task = PipelineTask(
            pipeline,
            params=PipelineParams(
                allow_interruptions=True,       # barge-in support
                enable_metrics=True,
                enable_usage_metrics=True,
            ),
        )

        # ── Event handlers ────────────────────────────────────────────────────
        @transport.event_handler("on_client_connected")
        async def on_connected(transport_obj, client):
            call_uuid = serializer.call_uuid or "pending"
            self._log.info("FreeSWITCH connected", call_uuid=call_uuid)
            self._latency.mark("client_connected")

            # Greet the caller immediately — inject a synthetic "Hello" so
            # the LLM produces an opening message without the caller speaking.
            await task.queue_frames(
                [
                    LLMMessagesUpdateFrame(
                        messages=[
                            {"role": "system", "content": self.config.system_prompt},
                            {"role": "user", "content": "Hello, I just picked up the phone."},
                        ],
                        run_llm=True,
                    )
                ]
            )

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
        await runner.run(task)

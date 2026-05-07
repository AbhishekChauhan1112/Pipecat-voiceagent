"""
ElevenLabs TTS Service wrapper.

Factory layer that constructs an ``ElevenLabsTTSService`` using the
WebSocket streaming API for minimal latency. Sentence-level aggregation
is used (the Pipecat default) which provides the best balance between
latency and audio quality.

Latency strategy:
  - ``eleven_turbo_v2_5`` model: ~75-100ms generation latency
  - WebSocket multi-stream API: audio chunks arrive as soon as generated
  - auto_mode=True: disables server-side buffering (best for sentences)
  - TTSService handles streaming chunks → AudioRawFrames automatically
"""

from loguru import logger

from pipecat.services.elevenlabs.tts import ElevenLabsTTSService

from src.config import AgentConfig


def build_elevenlabs_tts(config: AgentConfig) -> ElevenLabsTTSService:
    """Construct and return a configured ``ElevenLabsTTSService``.

    Uses the WebSocket streaming variant for lowest end-to-end latency.
    Audio arrives in chunks and is immediately pushed downstream without
    waiting for the full synthesis to complete.

    Args:
        config: Validated agent configuration object.

    Returns:
        A ready-to-use ``ElevenLabsTTSService`` instance.
    """
    logger.debug(
        "Building ElevenLabs TTS service",
        model=config.elevenlabs_model,
        voice_id=config.elevenlabs_voice_id,
    )

    tts = ElevenLabsTTSService(
        api_key=config.elevenlabs_api_key,
        voice_id=config.elevenlabs_voice_id,
        model=config.elevenlabs_model,
        sample_rate=16000,
        settings=ElevenLabsTTSService.Settings(
            stability=config.elevenlabs_stability,
            similarity_boost=config.elevenlabs_similarity_boost,
        ),
        # auto_mode=True is optimal for sentence-aggregated input
        # (disables server-side chunk scheduling for lower latency)
        auto_mode=True,
        # Enable ElevenLabs server-side request logging (disable in prod if needed)
        enable_logging=False,
    )

    logger.info(
        "ElevenLabs TTS service ready",
        model=config.elevenlabs_model,
        voice_id=config.elevenlabs_voice_id,
    )
    return tts

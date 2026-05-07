"""
Deepgram STT Service wrapper.

Thin factory layer that constructs a properly-configured
``DeepgramSTTService`` from the agent's central config.
All Deepgram-specific tuning lives here so the pipeline
orchestrator stays provider-agnostic.
"""

from loguru import logger

from pipecat.services.deepgram.stt import DeepgramSTTService
from pipecat.transcriptions.language import Language

from src.config import AgentConfig


def build_deepgram_stt(config: AgentConfig) -> DeepgramSTTService:
    """Construct and return a configured ``DeepgramSTTService``.

    Key capabilities enabled:
    - Real-time WebSocket streaming STT
    - Interim (partial) transcripts for responsiveness
    - Smart formatting & punctuation
    - Endpointing / VAD integration
    - Automatic keepalive & reconnection (handled by Pipecat internals)

    Args:
        config: Validated agent configuration object.

    Returns:
        A ready-to-use ``DeepgramSTTService`` instance.
    """
    logger.debug(
        "Building Deepgram STT service",
        model=config.deepgram_model,
        language=config.deepgram_language,
        endpointing_ms=config.deepgram_endpointing_ms,
    )

    # Map the string language code to Pipecat's Language enum.
    # Language enum values use underscore-separated BCP-47 tags (e.g. EN_US).
    try:
        # pipecat Language uses uppercase underscore format: "en-US" → "EN_US"
        lang_key = config.deepgram_language.upper().replace("-", "_")
        language = Language[lang_key]
    except KeyError:
        logger.warning(
            "Unknown language code, falling back to Language.EN",
            language=config.deepgram_language,
        )
        language = Language.EN

    stt = DeepgramSTTService(
        api_key=config.deepgram_api_key,
        encoding="linear16",
        channels=1,
        sample_rate=config.sample_rate,
        settings=DeepgramSTTService.Settings(
            model=config.deepgram_model,
            language=language,
            interim_results=True,
            smart_format=True,
            punctuate=True,
            endpointing=config.deepgram_endpointing_ms,
            utterance_end_ms=1000,
        ),
    )

    logger.info("Deepgram STT service ready")
    return stt

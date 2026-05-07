"""
Deepgram STT Service wrapper — Pipecat 0.0.108.

Uses LiveOptions directly (Pipecat's own LiveOptions type, not the Deepgram SDK one)
to construct the connection, bypassing the Settings class which has caused 400 errors.
"""

from loguru import logger

from pipecat.services.deepgram.stt import DeepgramSTTService, LiveOptions

from src.config import AgentConfig


def build_deepgram_stt(config: AgentConfig) -> DeepgramSTTService:
    """Construct and return a configured DeepgramSTTService.

    Uses live_options directly instead of Settings to avoid parameter
    mapping issues that caused 400 WebSocket errors in Pipecat 0.0.108.
    """
    logger.debug(
        "Building Deepgram STT service",
        model=config.deepgram_model,
        language=config.deepgram_language,
        sample_rate=config.sample_rate,
    )

    stt = DeepgramSTTService(
        api_key=config.deepgram_api_key,
        live_options=LiveOptions(
            model=config.deepgram_model,
            language=config.deepgram_language,   # plain string "en-US"
            encoding="linear16",
            channels=1,
            sample_rate=config.sample_rate,
            interim_results=True,
            smart_format=True,
            punctuate=True,
            endpointing=config.deepgram_endpointing_ms,
            utterance_end_ms=1000,
        ),
    )

    logger.info("Deepgram STT service ready")
    return stt

"""
Groq Whisper STT Service wrapper — fallback for Deepgram WebSocket issues.

Uses Groq's Whisper-large-v3-turbo via pipecat.services.groq.stt.
Same Groq API key as the LLM — no extra credentials needed.
"""

from loguru import logger

from pipecat.services.groq.stt import GroqSTTService

from src.config import AgentConfig


def build_groq_stt(config: AgentConfig) -> GroqSTTService:
    """Construct a GroqSTTService using Whisper-large-v3-turbo."""
    logger.debug("Building Groq Whisper STT service")

    stt = GroqSTTService(
        api_key=config.groq_api_key,
        model="whisper-large-v3-turbo",
    )

    logger.info("Groq Whisper STT service ready")
    return stt

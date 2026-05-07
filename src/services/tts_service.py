"""
ElevenLabs TTS Service wrapper.
"""

from loguru import logger

from pipecat.services.elevenlabs.tts import ElevenLabsTTSService

from src.config import AgentConfig


def build_elevenlabs_tts(config: AgentConfig) -> ElevenLabsTTSService:

    logger.info("Building ElevenLabs TTS service")

    tts = ElevenLabsTTSService(
        api_key=config.elevenlabs_api_key,

        voice_id=config.elevenlabs_voice_id,

        model=config.elevenlabs_model,

        sample_rate=16000,

        stability=config.elevenlabs_stability,

        similarity_boost=config.elevenlabs_similarity_boost,

        streaming_latency=0,
    )

    logger.info(
        f"ElevenLabs TTS ready "
        f"model={config.elevenlabs_model} "
        f"voice={config.elevenlabs_voice_id}"
    )

    return tts
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

        sample_rate=16000,

        params=ElevenLabsTTSService.InputParams(
            language="en",
            stability=config.elevenlabs_stability,
            similarity_boost=config.elevenlabs_similarity_boost,
        ),

        settings=ElevenLabsTTSService.Settings(
            voice=config.elevenlabs_voice_id,
            model=config.elevenlabs_model,
        ),
    )

    logger.info(
        f"ElevenLabs TTS ready "
        f"model={config.elevenlabs_model} "
        f"voice={config.elevenlabs_voice_id}"
    )

    return tts
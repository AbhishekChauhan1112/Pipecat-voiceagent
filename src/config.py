"""
Pipecat Realtime Voice Agent
============================
Configuration management using Pydantic Settings.
All values read from environment variables (or .env file).
"""

import os
from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AgentConfig(BaseSettings):
    """Central configuration for the voice agent.

    All fields are loaded from environment variables or the .env file.
    Validation is performed at startup to catch missing/invalid config early.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── API Keys ────────────────────────────────────────────────────────────
    deepgram_api_key: str = Field(..., description="Deepgram API key for STT")
    groq_api_key: str = Field(..., description="Groq API key for LLM inference")
    elevenlabs_api_key: str = Field(..., description="ElevenLabs API key for TTS")

    # ── Server ──────────────────────────────────────────────────────────────
    host: str = Field(default="0.0.0.0", description="Server bind host")
    port: int = Field(default=8765, description="Server WebSocket port")

    # ── Agent Personality ───────────────────────────────────────────────────
    agent_name: str = Field(default="Aria", description="Assistant display name")
    system_prompt: str = Field(
        default=(
            "You are Aria, a friendly and intelligent AI voice assistant. "
            "You are helpful, concise, and conversational. Keep your responses "
            "brief and natural — this is a voice conversation, so avoid long "
            "explanations unless asked. Respond directly and warmly."
        ),
        description="LLM system prompt defining personality",
    )

    # ── Audio ────────────────────────────────────────────────────────────────
    sample_rate: int = Field(default=16000, description="PCM audio sample rate in Hz")

    # ── Groq / LLM ──────────────────────────────────────────────────────────
    groq_model: str = Field(
        default="llama-3.3-70b-versatile", description="Groq model identifier"
    )
    llm_temperature: float = Field(
        default=0.7, ge=0.0, le=2.0, description="LLM generation temperature"
    )
    llm_max_tokens: int = Field(
        default=500, ge=1, description="Max LLM tokens per response"
    )

    # ── Deepgram / STT ──────────────────────────────────────────────────────
    deepgram_model: str = Field(
        default="nova-3-general", description="Deepgram transcription model"
    )
    deepgram_language: str = Field(
        default="en-US", description="BCP-47 language code for STT"
    )
    deepgram_endpointing_ms: int = Field(
        default=300, ge=0, description="Silence ms before Deepgram sends final transcript"
    )

    # ── ElevenLabs / TTS ────────────────────────────────────────────────────
    elevenlabs_voice_id: str = Field(
        default="21m00Tcm4TlvDq8ikWAM", description="ElevenLabs voice ID"
    )
    elevenlabs_model: str = Field(
        default="eleven_turbo_v2_5", description="ElevenLabs TTS model"
    )
    elevenlabs_stability: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Voice stability"
    )
    elevenlabs_similarity_boost: float = Field(
        default=0.75, ge=0.0, le=1.0, description="Voice similarity boost"
    )

    # ── Logging ──────────────────────────────────────────────────────────────
    log_level: Literal["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"] = Field(
        default="INFO", description="Logging level"
    )
    log_file: str = Field(
        default="logs/agent.log", description="Path to log file (directory created if missing)"
    )

    @field_validator("deepgram_api_key", "groq_api_key", "elevenlabs_api_key")
    @classmethod
    def api_key_not_placeholder(cls, v: str, info) -> str:  # noqa: N805
        """Reject placeholder values that were never replaced."""
        if v.startswith("your_") and v.endswith("_here"):
            raise ValueError(
                f"{info.field_name} still contains the placeholder value. "
                "Please set it in your .env file."
            )
        return v


@lru_cache(maxsize=1)
def get_config() -> AgentConfig:
    """Return a cached singleton AgentConfig instance.

    Using lru_cache means the .env file is only parsed once per process
    lifetime, which is safe for production deployments.
    """
    return AgentConfig()

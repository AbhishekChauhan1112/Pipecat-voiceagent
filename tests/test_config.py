"""
Tests for configuration management.

Run with:  pytest tests/ -v
"""

import os
import pytest
from unittest.mock import patch


def test_config_loads_with_env_vars():
    """Config should load cleanly when all required keys are present."""
    env = {
        "DEEPGRAM_API_KEY": "dg_test_key_abc123",
        "GROQ_API_KEY": "gsk_test_key_abc123",
        "ELEVENLABS_API_KEY": "el_test_key_abc123",
    }
    with patch.dict(os.environ, env, clear=False):
        # Force re-import to bypass lru_cache
        from importlib import import_module, reload
        import src.config as cfg_mod
        reload(cfg_mod)
        config = cfg_mod.AgentConfig(**env)  # type: ignore[call-arg]
        assert config.deepgram_api_key == "dg_test_key_abc123"
        assert config.groq_model == "llama-3.3-70b-versatile"
        assert config.sample_rate == 16000


def test_config_rejects_placeholder_keys():
    """Config should raise ValueError when placeholder API keys are used."""
    from pydantic import ValidationError
    env = {
        "DEEPGRAM_API_KEY": "your_deepgram_api_key_here",
        "GROQ_API_KEY": "gsk_real_key",
        "ELEVENLABS_API_KEY": "el_real_key",
    }
    with pytest.raises(ValidationError):
        from src.config import AgentConfig
        AgentConfig(**env)  # type: ignore[call-arg]


def test_config_defaults():
    """All optional fields should have sensible defaults."""
    env = {
        "DEEPGRAM_API_KEY": "dg_real_key",
        "GROQ_API_KEY": "gsk_real_key",
        "ELEVENLABS_API_KEY": "el_real_key",
    }
    from src.config import AgentConfig
    config = AgentConfig(**env)  # type: ignore[call-arg]
    assert config.host == "0.0.0.0"
    assert config.port == 8765
    assert config.log_level == "INFO"
    assert 0.0 <= config.llm_temperature <= 2.0
    assert config.llm_max_tokens > 0

"""
Tests for the FastAPI transport server.
"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch


def _make_test_env():
    return {
        "DEEPGRAM_API_KEY": "dg_real_key_abc",
        "GROQ_API_KEY": "gsk_real_key_abc",
        "ELEVENLABS_API_KEY": "el_real_key_abc",
    }


@pytest.fixture()
def client():
    import os
    env = _make_test_env()
    with patch.dict(os.environ, env, clear=False):
        from src.config import AgentConfig
        from src.transport.server import create_app
        config = AgentConfig(**env)  # type: ignore[call-arg]
        app = create_app(config=config)
        with TestClient(app) as c:
            yield c


def test_health_endpoint(client):
    """GET /health should return 200 with healthy status."""
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "healthy"
    assert "timestamp" in body


def test_info_endpoint(client):
    """GET /info should return agent configuration."""
    resp = client.get("/info")
    assert resp.status_code == 200
    body = resp.json()
    assert "agent_name" in body
    assert "models" in body
    assert "stt" in body["models"]
    assert "llm" in body["models"]
    assert "tts" in body["models"]

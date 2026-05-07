"""
FastAPI server — Telephony transport layer.

This server accepts WebSocket connections from FreeSWITCH mod_audio_stream
and hands each connection to an isolated TelephonyAgentPipeline.

Endpoints
─────────
  GET /health   → liveness probe (FreeSWITCH can poll this)
  GET /info     → public agent info
  WS  /        → audio stream endpoint (mod_audio_stream default, no path)
  WS  /ws       → audio stream endpoint (same handler, explicit path)

Security note:
  In production (or even for this POC) bind to 127.0.0.1 only (HOST=127.0.0.1
  in .env). FreeSWITCH and Pipecat run on the same machine and talk over
  loopback — this port should never be reachable from the internet.
"""

import asyncio
from datetime import datetime, timezone

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger

from src.config import AgentConfig, get_config
from src.pipeline.agent_pipeline import TelephonyAgentPipeline


def create_app(config: AgentConfig | None = None) -> FastAPI:
    """Create and configure the FastAPI telephony server application."""
    cfg = config or get_config()

    app = FastAPI(
        title="Pipecat Telephony Voice Agent",
        description=(
            "Realtime AI voice agent for FreeSWITCH — "
            "Deepgram STT + Groq LLM + ElevenLabs TTS"
        ),
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── Startup / shutdown ────────────────────────────────────────────────────
    @app.on_event("startup")
    async def on_startup() -> None:
        logger.info(
            "Telephony agent server starting",
            bind=f"{cfg.host}:{cfg.port}",
            agent=cfg.agent_name,
            stt=cfg.deepgram_model,
            llm=cfg.groq_model,
            tts=cfg.elevenlabs_model,
        )

    @app.on_event("shutdown")
    async def on_shutdown() -> None:
        logger.info("Telephony agent server shutting down")

    # ── REST endpoints ────────────────────────────────────────────────────────

    @app.get("/health", tags=["Monitoring"])
    async def health() -> JSONResponse:
        """Liveness probe — returns 200 when the server is up."""
        return JSONResponse(
            {
                "status": "healthy",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "service": "pipecat-telephony-agent",
            }
        )

    @app.get("/info", tags=["Monitoring"])
    async def info() -> JSONResponse:
        """Return public agent configuration (no secrets)."""
        return JSONResponse(
            {
                "agent_name": cfg.agent_name,
                "models": {
                    "stt": cfg.deepgram_model,
                    "llm": cfg.groq_model,
                    "tts": cfg.elevenlabs_model,
                },
                "sample_rate": cfg.sample_rate,
                "transport": "FreeSWITCH mod_audio_stream",
            }
        )

    # ── WebSocket handler (shared logic) ─────────────────────────────────────

    async def _handle_call(websocket: WebSocket) -> None:
        """Core call handler — shared by both WebSocket routes.

        Each WebSocket connection = one isolated phone call.

        Audio protocol (binary, no framing):
          FreeSWITCH → Pipecat : binary PCM16 frames (L16, 16 kHz, mono)
          Pipecat → FreeSWITCH : binary PCM16 frames (same format)
        """
        await websocket.accept()
        client = websocket.client.host if websocket.client else "freeswitch"
        path  = websocket.url.path
        logger.info("Incoming call — WebSocket accepted", client=client, path=path)

        pipeline = TelephonyAgentPipeline(websocket=websocket, config=cfg)
        try:
            await pipeline.run()
        except WebSocketDisconnect:
            logger.info("Call ended — WebSocket closed cleanly", client=client)
        except asyncio.CancelledError:
            logger.info("Pipeline cancelled", client=client)
        except Exception as exc:
            logger.exception("Call pipeline error", client=client, error=str(exc))
            try:
                await websocket.close(code=1011)
            except Exception:
                pass

    # ── WebSocket endpoints ───────────────────────────────────────────────────
    # Two routes, same handler:
    #   /    ← what the existing Lua script uses (ws://127.0.0.1:8765)
    #   /ws  ← explicit path for clarity / future clients

    @app.websocket("/")
    async def call_endpoint_root(websocket: WebSocket) -> None:
        """Root WebSocket — FreeSWITCH Lua uses ws://127.0.0.1:8765 (no path)."""
        await _handle_call(websocket)

    @app.websocket("/ws")
    async def call_endpoint(websocket: WebSocket) -> None:
        """Explicit /ws path for documentation and alternative clients."""
        await _handle_call(websocket)

    return app

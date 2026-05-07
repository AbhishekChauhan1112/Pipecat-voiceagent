"""
main.py — Pipecat Telephony Voice Agent entry point.

Starts a FastAPI/Uvicorn WebSocket server that FreeSWITCH mod_audio_stream
connects to when Linphone calls extension 9000.

Usage:
    python main.py                        # reads .env
    python main.py --host 127.0.0.1 --port 8765
    python main.py --log-level DEBUG      # verbose output for debugging
"""

import argparse
import sys

import uvicorn
from loguru import logger

from src.config import get_config
from src.logging_utils import setup_logging
from src.transport.server import create_app


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pipecat Telephony Voice Agent (FreeSWITCH + Deepgram + Groq + ElevenLabs)"
    )
    p.add_argument("--host", default=None, help="Override HOST from .env")
    p.add_argument("--port", type=int, default=None, help="Override PORT from .env")
    p.add_argument(
        "--log-level",
        choices=["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"],
        default=None,
    )
    p.add_argument("--reload", action="store_true", help="Hot-reload on code change (dev)")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # ── Load config ───────────────────────────────────────────────────────────
    try:
        config = get_config()
    except Exception as exc:
        print(f"\n❌  Config error: {exc}", file=sys.stderr)
        print("  → Copy .env.example to .env and fill in your API keys.\n", file=sys.stderr)
        sys.exit(1)

    host      = args.host      or config.host
    port      = args.port      or config.port
    log_level = args.log_level or config.log_level

    # ── Logging ───────────────────────────────────────────────────────────────
    setup_logging(log_level=log_level, log_file=config.log_file)

    logger.info("╔══════════════════════════════════════════════╗")
    logger.info("║   Pipecat Telephony Voice Agent  v1.0.0      ║")
    logger.info("╚══════════════════════════════════════════════╝")
    logger.info(f"  Agent        : {config.agent_name}")
    logger.info(f"  STT          : Groq Whisper ({config.groq_model})")
    logger.info(f"  LLM          : Groq {config.groq_model}")
    logger.info(f"  TTS          : ElevenLabs {config.elevenlabs_model}")
    logger.info(f"  Sample rate  : {config.sample_rate} Hz")
    logger.info(f"  WebSocket    : ws://{host}:{port}/ws  ← FreeSWITCH connects here")
    logger.info(f"  Health       : http://{host}:{port}/health")
    logger.info("")
    logger.info("  Waiting for Linphone to call extension 9000 on FreeSWITCH…")

    # ── Run ───────────────────────────────────────────────────────────────────
    app = create_app(config=config)
    server = uvicorn.Server(
        uvicorn.Config(
            app=app,
            host=host,
            port=port,
            log_level=log_level.lower(),
            lifespan="on",
            ws_max_size=16 * 1024 * 1024,
            reload=args.reload,
            reload_dirs=["src"] if args.reload else None,
        )
    )
    try:
        server.run()
    except KeyboardInterrupt:
        logger.info("Server stopped.")


if __name__ == "__main__":
    main()

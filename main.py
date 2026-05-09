"""
main.py — Pipecat Telephony Voice Agent entry point.

Supports two transports:
  --transport websocket  (default)
      FreeSWITCH mod_audio_stream → WebSocket ws://127.0.0.1:8765 → Pipecat
      Start with: python main.py --transport websocket

  --transport janus
      FreeSWITCH → Janus AudioBridge → aiortc → Pipecat
      Start with: python main.py --transport janus

Usage:
        python main.py                              # websocket transport (mod_audio_stream)
        python main.py --transport janus            # Janus/aiortc transport
        python main.py --log-level DEBUG            # verbose output
"""

import argparse
import asyncio
import sys

from loguru import logger

from src.config import get_config
from src.logging_utils import setup_logging


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pipecat Telephony Voice Agent"
    )
    p.add_argument(
        "--transport",
        choices=["websocket", "janus"],
        default="websocket",
        help="websocket = mod_audio_stream (default); janus = Janus AudioBridge/aiortc",
    )
    p.add_argument(
        "--log-level",
        choices=["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"],
        default=None,
    )
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
    logger.info(f"  Transport    : {args.transport}")

    # ── Run ───────────────────────────────────────────────────────────────────
    try:
        if args.transport == "websocket":
            from src.transport.websocket.ws_transport import run_ws_manager
            logger.info("  Listening on : ws://0.0.0.0:8765")
            logger.info("")
            logger.info("  Waiting for FreeSWITCH mod_audio_stream connection…")
            asyncio.run(run_ws_manager(config))

        else:
            import logging as _stdlib_logging
            _stdlib_logging.basicConfig(level=_stdlib_logging.DEBUG)
            _stdlib_logging.getLogger("aiortc").setLevel(_stdlib_logging.DEBUG)
            _stdlib_logging.getLogger("aioice").setLevel(_stdlib_logging.DEBUG)

            from src.transport.janus.config import ROOM_ID
            from src.transport.janus.transport_manager import run_manager
            logger.info(f"  Room         : {ROOM_ID}")
            logger.info("")
            logger.info("  Waiting for Linphone to call via FreeSWITCH…")
            asyncio.run(run_manager(config))

    except KeyboardInterrupt:
        logger.info("Service stopped.")


if __name__ == "__main__":
    main()

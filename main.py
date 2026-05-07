"""
main.py — Pipecat Telephony Voice Agent entry point.

Starts the Janus WebRTC transport manager which bridges:
    FreeSWITCH RTP → Janus AudioBridge → aiortc → Pipecat pipeline.

Usage:
        python main.py                        # reads .env
        python main.py --log-level DEBUG      # verbose output for debugging
"""

import argparse
import asyncio
import sys

from loguru import logger

from src.config import get_config
from src.logging_utils import setup_logging
from src.transport.janus.config import ROOM_ID
from src.transport.janus.transport_manager import run_manager


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Pipecat Telephony Voice Agent (Janus + Deepgram + Groq + ElevenLabs)"
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
    logger.info("  Transport    : Janus AudioBridge via aiortc")
    logger.info(f"  Room         : {ROOM_ID}")
    logger.info("")
    logger.info("  Waiting for Linphone to call via FreeSWITCH…")

    # ── Run ───────────────────────────────────────────────────────────────────
    try:
        asyncio.run(run_manager(config))
    except KeyboardInterrupt:
        logger.info("Service stopped.")


if __name__ == "__main__":
    main()

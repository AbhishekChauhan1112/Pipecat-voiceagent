"""
Logging utilities for the Pipecat Voice Agent.

Configures Loguru with:
  - Structured JSON output for production use
  - Human-readable console output for development
  - Per-session context binding for tracing individual calls
  - Latency measurement helpers
"""

import sys
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from loguru import logger


def setup_logging(log_level: str = "INFO", log_file: str = "logs/agent.log") -> None:
    """Configure Loguru sinks for console and file output.

    Args:
        log_level: Minimum log level string (e.g. "INFO", "DEBUG").
        log_file:  Path to the rotating log file. Parent directories are
                   created automatically.
    """
    # Remove default handler
    logger.remove()

    # ── Console sink (human-readable) ───────────────────────────────────────
    logger.add(
        sys.stderr,
        level=log_level,
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "<level>{message}</level>"
        ),
        colorize=True,
        enqueue=True,  # thread-safe async-safe
    )

    # ── File sink (structured JSON for production monitoring) ───────────────
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger.add(
        str(log_path),
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name}:{function}:{line} | {message}",
        rotation="50 MB",
        retention="7 days",
        compression="gz",
        serialize=True,      # JSON lines format
        enqueue=True,
        backtrace=True,
        diagnose=False,      # disable in prod to avoid leaking locals
    )

    logger.info("Logging initialised", log_level=log_level, log_file=str(log_path))


def get_session_logger(session_id: str):
    """Return a logger pre-bound with a session_id context variable.

    Usage::

        log = get_session_logger("abc-123")
        log.info("Pipeline started")   # => includes session_id="abc-123"
    """
    return logger.bind(session_id=session_id)


class LatencyTracker:
    """Measures and logs wall-clock latency for named pipeline stages.

    Usage::

        tracker = LatencyTracker(session_id="abc-123")
        with tracker.measure("stt"):
            ...   # code to time
        tracker.log_summary()
    """

    def __init__(self, session_id: str) -> None:
        self.session_id = session_id
        self._marks: dict[str, float] = {}
        self.measurements: dict[str, float] = {}
        self._log = get_session_logger(session_id)

    def mark(self, name: str) -> None:
        """Record a named timestamp (ms since epoch)."""
        self._marks[name] = time.monotonic() * 1000

    def record(self, name: str, start_name: str) -> float:
        """Calculate elapsed ms between two marks and store it."""
        start = self._marks.get(start_name)
        end = time.monotonic() * 1000
        if start is None:
            self._log.warning("LatencyTracker: start mark not found", mark=start_name)
            return 0.0
        elapsed = end - start
        self.measurements[name] = elapsed
        self._log.debug(
            "Latency measurement",
            stage=name,
            elapsed_ms=round(elapsed, 2),
        )
        return elapsed

    @contextmanager
    def measure(self, stage: str) -> Generator[None, None, None]:
        """Context manager that automatically records elapsed time."""
        start = time.monotonic() * 1000
        try:
            yield
        finally:
            elapsed = time.monotonic() * 1000 - start
            self.measurements[stage] = elapsed
            self._log.debug(
                "Latency measurement",
                stage=stage,
                elapsed_ms=round(elapsed, 2),
            )

    def log_summary(self) -> None:
        """Emit a single summary log line with all recorded measurements."""
        if not self.measurements:
            return
        summary = {k: round(v, 2) for k, v in self.measurements.items()}
        total = round(sum(self.measurements.values()), 2)
        self._log.info(
            "Latency summary",
            latency_ms=summary,
            total_pipeline_ms=total,
        )

"""
FreeSWITCH mod_audio_stream WebSocket Serializer.

This serializer translates between:
  • FreeSWITCH mod_audio_stream binary protocol (raw PCM16 over WebSocket)
  • Pipecat's internal InputAudioRawFrame / AudioRawFrame

Protocol breakdown
──────────────────
When a call hits the FreeSWITCH dialplan extension:

  1. FreeSWITCH sends one JSON text message (the handshake):
       {"hostname":"fs01","uuid":"<call-uuid>","channels":1,"rate":16000,"codec":"L16"}

  2. FreeSWITCH then streams BINARY WebSocket messages containing raw
     L16 (linear 16-bit PCM) audio sampled at the configured rate.

  3. To play audio BACK to the caller, this server sends BINARY
     WebSocket messages containing the same format: raw L16 PCM bytes.

No headers, no framing, no base64 — just raw bytes in both directions.

Usage
─────
    serializer = FreeSwitchAudioSerializer(sample_rate=16000)
    transport = FastAPIWebsocketTransport(..., params=FastAPIWebsocketParams(
        serializer=serializer,
        ...
    ))
"""

import json
from typing import Optional

from loguru import logger

from pipecat.frames.frames import AudioRawFrame, Frame, InputAudioRawFrame
from pipecat.serializers.base_serializer import FrameSerializer


class FreeSwitchAudioSerializer(FrameSerializer):
    """Pipecat FrameSerializer for FreeSWITCH mod_audio_stream protocol.

    Handles:
      - JSON handshake (first message) → extracts call UUID and codec info
      - Binary PCM frames → InputAudioRawFrame (audio INTO the pipeline)
      - AudioRawFrame → bytes (audio OUT to FreeSWITCH / the caller)

    Args:
        sample_rate: Expected PCM sample rate in Hz. Must match the value
                     configured in the FreeSWITCH dialplan audio_stream action.
                     Default: 16000 (16 kHz, best quality for Deepgram).
        num_channels: Number of audio channels. FreeSWITCH mod_audio_stream
                      always delivers mono (1 channel) for voice calls.
    """

    def __init__(self, sample_rate: int = 16000, num_channels: int = 1) -> None:
        self._sample_rate = sample_rate
        self._num_channels = num_channels
        self._handshake_done: bool = False
        self._call_uuid: Optional[str] = None

    # ── Public helpers ────────────────────────────────────────────────────

    @property
    def call_uuid(self) -> Optional[str]:
        """Return the FreeSWITCH call UUID received in the handshake."""
        return self._call_uuid

    @property
    def sample_rate(self) -> int:
        return self._sample_rate

    # ── FrameSerializer interface ─────────────────────────────────────────

    async def serialize(self, frame: Frame) -> bytes | str | None:
        """Convert a Pipecat audio frame → raw PCM bytes for FreeSWITCH.

        Only AudioRawFrame instances produce output; all other frame types
        are silently dropped (they have no meaning in the raw-PCM channel).

        Args:
            frame: Any Pipecat Frame (only AudioRawFrame is acted upon).

        Returns:
            Raw PCM16 bytes to send back through the WebSocket to
            FreeSWITCH, or None to send nothing.
        """
        if isinstance(frame, AudioRawFrame):
            return frame.audio
        return None

    async def deserialize(self, data: str | bytes) -> Frame | None:
        """Convert a FreeSWITCH WebSocket message → Pipecat Frame.

        Handles two message types:
          - str  → JSON handshake (first message, no frame produced)
          - bytes → raw PCM16 audio (produces InputAudioRawFrame)

        Args:
            data: Raw WebSocket message from FreeSWITCH.

        Returns:
            InputAudioRawFrame for binary audio messages, or None for the
            JSON handshake / empty frames.
        """
        # ── JSON handshake (text frame) ───────────────────────────────────
        if isinstance(data, str):
            self._handle_handshake(data)
            return None

        # ── Binary audio frame ────────────────────────────────────────────
        if not isinstance(data, bytes) or len(data) == 0:
            return None

        return InputAudioRawFrame(
            audio=data,
            num_channels=self._num_channels,
            sample_rate=self._sample_rate,
        )

    # ── Private helpers ───────────────────────────────────────────────────

    def _handle_handshake(self, raw: str) -> None:
        """Parse the JSON metadata message sent by mod_audio_stream."""
        try:
            meta: dict = json.loads(raw)
        except json.JSONDecodeError as exc:
            logger.warning(
                "FreeSwitchAudioSerializer: could not parse handshake JSON",
                error=str(exc),
                raw=raw[:200],
            )
            return

        self._call_uuid = meta.get("uuid")
        self._handshake_done = True

        # Log the effective rate so mismatches are immediately visible
        reported_rate = meta.get("rate", "?")
        if reported_rate != "?" and int(reported_rate) != self._sample_rate:
            logger.warning(
                "FreeSWITCH sample rate mismatch — audio quality may be degraded. "
                "Update the dialplan or SAMPLE_RATE in .env to match.",
                freeswitch_rate=reported_rate,
                pipecat_expected_rate=self._sample_rate,
            )

        logger.info(
            "FreeSWITCH call connected",
            call_uuid=self._call_uuid,
            hostname=meta.get("hostname", "?"),
            codec=meta.get("codec", "L16"),
            rate=reported_rate,
            channels=meta.get("channels", 1),
        )

"""
FreeSWITCH mod_audio_stream WebSocket Serializer.

This serializer translates between:
  • FreeSWITCH mod_audio_stream binary protocol (raw PCM16 over WebSocket)
  • Pipecat's internal InputAudioRawFrame / AudioRawFrame

Protocol breakdown (stereo mode)
──────────────────────────────────
When pipecat.lua calls `uuid_audio_stream start <url> stereo 16000`:

  1. FreeSWITCH sends one JSON text message (the handshake):
       {"hostname":"fs01","uuid":"<call-uuid>","channels":2,"rate":16000,"codec":"L16"}

  2. FreeSWITCH streams BINARY WebSocket messages containing INTERLEAVED
     stereo L16 PCM (left=caller audio, right=silence/unused) at 16kHz.
     We extract just the LEFT channel for STT processing.

  3. To play audio BACK to the caller, we send BINARY WebSocket messages
     containing MONO L16 PCM at 16kHz. mod_audio_stream routes this to the
     write side of the media bug (SMBF_WRITE_STREAM) → OPUS encoder → caller.

  ⚠ stereo mode MUST be used in pipecat.lua (not mono) because mono only
    sets SMBF_READ_STREAM, which captures audio from caller but does NOT
    enable write-back. Only stereo sets SMBF_WRITE_STREAM.

No WAV headers, no base64 — just raw bytes in both directions.
"""

import json
import struct
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
        self._rx_packets = 0      # binary frames received from FreeSWITCH
        self._tx_packets = 0      # binary frames sent to FreeSWITCH
        self._rx_bytes   = 0
        self._tx_bytes   = 0

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
        """Convert a Pipecat audio frame → raw PCM bytes for FreeSWITCH."""
        if isinstance(frame, AudioRawFrame):
            out_audio = frame.audio

            # If FreeSWITCH expects stereo, we must duplicate the mono TTS audio
            # into left and right channels for playback
            if self._num_channels == 2 and len(out_audio) >= 2:
                # Fast mono->stereo duplication: copy each 2-byte sample
                pairs = [out_audio[i:i+2] for i in range(0, len(out_audio), 2)]
                out_audio = b''.join(p + p for p in pairs)

            self._tx_packets += 1
            self._tx_bytes += len(out_audio)
            
            if self._tx_packets == 1:
                logger.info(
                    "Serializer: first audio OUT packet sent to FreeSWITCH",
                    bytes=len(out_audio),
                    sample_rate=frame.sample_rate,
                    channels=self._num_channels,
                )
            elif self._tx_packets % 200 == 0:
                logger.debug(
                    "Serializer: audio OUT stats",
                    packets=self._tx_packets,
                    total_bytes=self._tx_bytes,
                )
            return out_audio
        return None

    async def deserialize(self, data: str | bytes) -> Frame | None:
        """Convert a FreeSWITCH WebSocket message → Pipecat Frame."""
        # ── JSON handshake (text frame) ───────────────────────────────────
        if isinstance(data, str):
            logger.debug("Serializer: received text frame (handshake)", raw=data[:200])
            self._handle_handshake(data)
            return None

        # ── Binary audio frame ────────────────────────────────────────────
        if not isinstance(data, bytes) or len(data) == 0:
            logger.debug("Serializer: empty/non-bytes frame", dtype=type(data).__name__)
            return None

        self._rx_packets += 1
        self._rx_bytes += len(data)

        if self._rx_packets == 1:
            logger.debug(
                "Serializer: FIRST audio IN packet — FreeSWITCH is streaming",
                bytes=len(data),
                channels=self._num_channels,
            )
        elif self._rx_packets % 200 == 0:
            logger.debug(
                "Serializer: audio IN stats",
                packets=self._rx_packets,
                total_bytes=self._rx_bytes,
            )

        # Stereo interleaved → extract left channel (caller audio) for STT.
        # FreeSWITCH stereo: [L0 R0 L1 R1 ...] as int16 little-endian pairs.
        # We take every even sample (index 0, 2, 4, ...) = left = caller.
        if self._num_channels == 2 and len(data) >= 4:
            samples = struct.unpack_from(f"<{len(data)//2}h", data)
            mono_samples = samples[::2]  # left channel only
            mono_data = struct.pack(f"<{len(mono_samples)}h", *mono_samples)
            logger.debug(
                "Serializer: stereo→mono downmix",
                stereo_bytes=len(data),
                mono_bytes=len(mono_data),
            ) if self._rx_packets == 1 else None
        else:
            mono_data = data

        return InputAudioRawFrame(
            audio=mono_data,
            num_channels=1,
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

        # Auto-detect channel count from handshake (1=mono, 2=stereo)
        reported_channels = int(meta.get("channels", self._num_channels))
        if reported_channels != self._num_channels:
            logger.info(
                f"FreeSWITCH sent channels={reported_channels}, "
                f"updating serializer (was {self._num_channels}). "
                f"{'Stereo→mono downmix enabled.' if reported_channels == 2 else ''}"
            )
            self._num_channels = reported_channels

        # Log rate mismatches immediately
        reported_rate = meta.get("rate", "?")
        if reported_rate != "?" and int(reported_rate) != self._sample_rate:
            logger.warning(
                "FreeSWITCH sample rate mismatch — audio quality may be degraded.",
                freeswitch_rate=reported_rate,
                pipecat_expected_rate=self._sample_rate,
            )

        logger.info(
            "FreeSWITCH call connected",
            call_uuid=self._call_uuid,
            hostname=meta.get("hostname", "?"),
            codec=meta.get("codec", "L16"),
            rate=reported_rate,
            channels=self._num_channels,
        )


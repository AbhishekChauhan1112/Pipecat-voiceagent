import asyncio
import logging
import traceback
import fractions

from aiortc import RTCPeerConnection, RTCSessionDescription, AudioStreamTrack, MediaStreamTrack
from aiortc.sdp import candidate_from_sdp
import av
from av import AudioFrame
import math
import numpy as np
from fractions import Fraction


class SilentAudioTrack(MediaStreamTrack):
    """Sends silent PCM frames so aiortc negotiates sendrecv instead of recvonly."""

    kind = "audio"

    def __init__(self):
        super().__init__()
        self.sample_rate = 48000
        self.samples_per_frame = 960  # 20 ms @ 48 kHz
        self.timestamp = 0

    async def recv(self):
        await asyncio.sleep(0.02)

        frame = AudioFrame(
            format="s16",
            layout="stereo",
            samples=self.samples_per_frame,
        )

        frame.pts = self.timestamp
        frame.sample_rate = self.sample_rate
        frame.time_base = fractions.Fraction(1, self.sample_rate)

        self.timestamp += self.samples_per_frame

        for p in frame.planes:
            p.update(b"\x00" * p.buffer_size)

        return frame


class ToneAudioTrack(AudioStreamTrack):
    """Generates a stereo 440 Hz sine-wave at 48 kHz with a pure monotonic pts.

    CRITICAL: next_timestamp() is deliberately NOT called here.
    aiortc's next_timestamp() internally converts wall-clock nanoseconds to
    RTP 32-bit timestamps, which overflows and corrupts pts after a few seconds
    (observed: pts jumps from ~52800 to ~4295019136).
    We drive our own pts counter starting from 0, incrementing by
    samples_per_frame (960) every call.  Pacing is handled externally by
    the aiortc sender loop.
    """

    kind = "audio"

    def __init__(self):
        super().__init__()

        self.sample_rate = 48000
        self.samples_per_frame = 960  # 20 ms @ 48 kHz

        self.phase = 0
        self._pts = 0

        self.frequency = 440.0

        print("[TONE_TRACK] initialized — pure monotonic pts, NO next_timestamp()")

    async def recv(self):
        # ── Tone generation ────────────────────────────────────────────────
        t = (
            np.arange(self.samples_per_frame) + self.phase
        ) / self.sample_rate

        mono = (0.2 * np.sin(2 * math.pi * self.frequency * t) * 32767).astype(
            np.int16
        )

        # av.AudioFrame.from_ndarray with layout="stereo" expects shape
        # (2, samples) — channels-first — when format is "s16p" (planar).
        # For packed s16 interleaved, from_ndarray expects (samples, 2).
        # We use s16 (packed) so shape must be (samples, channels) = (960, 2).
        stereo = np.column_stack([mono, mono])  # shape: (960, 2)

        # ── Build frame ────────────────────────────────────────────────────
        frame = av.AudioFrame.from_ndarray(
            stereo,
            format="s16",
            layout="stereo",
        )

        frame.sample_rate = self.sample_rate
        frame.time_base = Fraction(1, self.sample_rate)
        frame.pts = self._pts

        # ── Advance counters AFTER assigning pts ───────────────────────────
        self._pts += self.samples_per_frame
        self.phase += self.samples_per_frame

        # ── Diagnostics ────────────────────────────────────────────────────
        print(
            "[FRAME_INFO]",
            frame.layout.name,   # expected: stereo
            frame.format.name,   # expected: s16
            frame.samples,       # expected: 960
            frame.sample_rate,   # expected: 48000
            frame.pts,           # expected: 0, 960, 1920, ...
        )

        return frame

from .audio_tracks import AudioReceiver
from . import config

logger = logging.getLogger(__name__)


class RTCTransport:
    def __init__(self, media_bridge=None):
        self.pc = None
        self.audio_receivers = []
        self.media_bridge = media_bridge
        self._audio_reader_tasks = set()
        self._stats_task = None
        self._audio_transceiver_added = False
        self.outbound_track = None
        self.initialize()

    def initialize(self):
        """Initialize a fresh PeerConnection if one is not active."""
        if self.pc and self.pc.connectionState != "closed":
            return
        self.pc = RTCPeerConnection()
        self._setup_events()

    def _setup_events(self):
        @self.pc.on("connectionstatechange")
        async def on_connectionstatechange():
            print(f"[PC] connectionState={self.pc.connectionState}")
            logger.warning("[PC] connectionState=%s", self.pc.connectionState)
            if self.pc.connectionState == "connected" and not self._stats_task:
                self._stats_task = asyncio.create_task(self._poll_stats())
                print("[TASK] creating task")
            if self.pc.connectionState == "failed":
                await self.pc.close()

        @self.pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            print(f"[PC] iceConnectionState={self.pc.iceConnectionState}")
            logger.warning("[PC] iceConnectionState=%s", self.pc.iceConnectionState)

        @self.pc.on("icegatheringstatechange")
        async def on_icegatheringstatechange():
            print(f"[PC] iceGatheringState={self.pc.iceGatheringState}")
            logger.warning("[PC] iceGatheringState=%s", self.pc.iceGatheringState)

        @self.pc.on("signalingstatechange")
        async def on_signalingstatechange():
            print(f"[PC] signalingState={self.pc.signalingState}")
            logger.warning("[PC] signalingState=%s", self.pc.signalingState)

        @self.pc.on("track")
        def on_track(track):
            print(f"[TRACK] kind={track.kind} id={track.id}")

            if track.kind == "audio":
                asyncio.create_task(self._read_audio(track))
            else:
                logger.warning("[TRACK_IGNORED] kind=%s id=%s", track.kind, track.id)

    # NOTE: _poll_stats is defined once below (the complete version that
    # also tracks inbound-rtp / remote-inbound-rtp stats).  This duplicate
    # stub has been removed.

    async def _read_audio(self, track):
        print("[AUDIO] reader started")

        while True:
            try:
                frame = await track.recv()

                print(
                    f"[AUDIO_FRAME] "
                    f"samples={frame.samples} "
                    f"rate={frame.sample_rate} "
                    f"layout={frame.layout.name} "
                    f"pts={frame.pts}"
                )

                if self.media_bridge:
                    await self.media_bridge.enqueue_inbound_frame(frame)

            except Exception as e:
                print(f"[AUDIO_RECV_ERROR] {repr(e)}")
                break

    def add_track(self, track):
        """Add a local MediaStreamTrack to the PeerConnection."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        for sender in self.pc.getSenders():
            if sender.track is track:
                logger.debug("Track already added, skipping duplicate sender")
                return

        logger.info("Adding local track: %s", track.kind)
        # self.pc.addTrack(track)

    async def create_offer(self) -> dict:
        """Create an SDP offer to send to Janus."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        logger.info("Creating SDP offer...")
        offer = await self.pc.createOffer()
        await self.pc.setLocalDescription(offer)

        # Wait for ICE gathering to complete or timeout.
        try:
            await asyncio.wait_for(self._wait_for_ice_gathering_complete(), timeout=2.0)
        except asyncio.TimeoutError:
            logger.warning(
                "Timeout waiting for ICE gathering to complete. "
                "Proceeding with gathered candidates."
            )

        return {"type": self.pc.localDescription.type, "sdp": self.pc.localDescription.sdp}

    async def _wait_for_ice_gathering_complete(self):
        if self.pc.iceGatheringState == "complete":
            return

        while self.pc.iceGatheringState != "complete":
            await asyncio.sleep(0.1)

    async def set_remote_answer(self, sdp: str, type: str = "answer"):
        """Set the remote description from Janus."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        logger.info("Setting remote description (answer)...")
        answer = RTCSessionDescription(sdp=sdp, type=type)
        await self.pc.setRemoteDescription(answer)

    async def generate_sip_answer(self, sip_offer_sdp: str) -> dict:
        """Generate a valid SDP answer for the Janus SIP plugin accept request.

        Uses a SEPARATE temporary RTCPeerConnection that is NOT self.pc.
        self.pc is exclusively reserved for the AudioBridge WebRTC peer.

        The temporary PC is closed after extracting the answer — Janus SIP
        plugin handles the actual SIP-side WebRTC transport internally.
        We only need to produce a valid answer SDP for signaling.
        """
        import traceback as _tb

        print("[AIORTC_CREATE_ANSWER] creating temporary SIP signaling PC")
        logger.warning("[AIORTC_CREATE_ANSWER] starting SIP offer/answer negotiation")

        sip_pc = RTCPeerConnection()
        try:
            # Consume SIP offer in the temporary PC only
            sip_offer = RTCSessionDescription(sdp=sip_offer_sdp, type="offer")
            print("[AIORTC_CREATE_ANSWER] setRemoteDescription (SIP offer)")
            await sip_pc.setRemoteDescription(sip_offer)

            # Generate answer
            print("[AIORTC_CREATE_ANSWER] createAnswer")
            answer = await sip_pc.createAnswer()

            print("[AIORTC_CREATE_ANSWER] setLocalDescription")
            await sip_pc.setLocalDescription(answer)

            # Wait for ICE gathering (short timeout — SIP plugin needs fast response)
            try:
                deadline = 3.0

                async def _wait():
                    while sip_pc.iceGatheringState != "complete":
                        await asyncio.sleep(0.05)

                await asyncio.wait_for(_wait(), timeout=deadline)
            except asyncio.TimeoutError:
                logger.warning("[AIORTC_CREATE_ANSWER] ICE gathering timeout — proceeding")

            local = sip_pc.localDescription
            logger.warning(
                "[AIORTC_LOCAL_DESCRIPTION_READY] type=%s sdp_start=%s",
                local.type,
                local.sdp[:300],
            )
            print("[AIORTC_LOCAL_DESCRIPTION_READY] type=", local.type)
            print("[AIORTC_LOCAL_DESCRIPTION_READY] sdp (first 300):", local.sdp[:300])

            # Defensive check
            if local.type != "answer":
                raise RuntimeError(
                    f"[AIORTC_CREATE_ANSWER] expected type='answer' got '{local.type}'"
                )

            return {"type": local.type, "sdp": local.sdp}

        except Exception as e:
            print("[AIORTC_CREATE_ANSWER_ERROR]", repr(e))
            _tb.print_exc()
            raise
        finally:
            # Close temp PC — AudioBridge PC (self.pc) is unaffected
            try:
                await sip_pc.close()
                print("[AIORTC_CREATE_ANSWER] temporary SIP PC closed")
            except Exception:
                pass



    async def join_audiobridge(self, offer_sdp: str) -> dict:
        """Consume an AudioBridge JSEP offer and return a WebRTC answer.

        This is the ONLY place aiortc consumes an SDP offer.
        The SIP plugin SDP is NEVER consumed here — SIP plugin is call-control only.
        AudioBridge acts as the actual WebRTC peer that forwards mixed room audio.
        """
        import traceback as _tb

        # Close any existing PC so each call starts fresh
        if self.pc is not None:
            try:
                await self.pc.close()
            except Exception:
                pass
            self.pc = None

        self.pc = RTCPeerConnection()
        self._setup_events()
        print("[AUDIOBRIDGE_PC] fresh RTCPeerConnection created")

        # Per-call state event hooks
        @self.pc.on("connectionstatechange")
        async def on_connectionstatechange():
            print("[PC_STATE]", self.pc.connectionState)
            logger.warning("[PC_STATE] connectionState=%s", self.pc.connectionState)

        @self.pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            print("[ICE_STATE]", self.pc.iceConnectionState)
            logger.warning("[ICE_STATE] iceConnectionState=%s", self.pc.iceConnectionState)

        @self.pc.on("signalingstatechange")
        async def on_signalingstatechange():
            print("[SIGNALING_STATE]", self.pc.signalingState)
            logger.warning("[SIGNALING_STATE] signalingState=%s", self.pc.signalingState)

        # Step 1: consume AudioBridge offer
        logger.warning("[AUDIOBRIDGE_OFFER] %s", offer_sdp)
        offer = RTCSessionDescription(sdp=offer_sdp, type="offer")
        print("[AUDIOBRIDGE_PC] setting remote description (AudioBridge offer)")
        try:
            await self.pc.setRemoteDescription(offer)
        except Exception as e:
            print("[FATAL_EXCEPTION] setRemoteDescription failed:", e)
            _tb.print_exc()
            raise
        print("[AUDIOBRIDGE_PC] remote description set")

        # Step 2: createAnswer (recvonly — no outbound track needed for AudioBridge)
        print("[AUDIOBRIDGE_PC] creating answer")
        try:
            answer = await self.pc.createAnswer()
        except Exception as e:
            print("[FATAL_EXCEPTION] createAnswer failed:", e)
            _tb.print_exc()
            raise
        print("[AUDIOBRIDGE_PC] answer created")

        # Step 3: setLocalDescription
        print("[AUDIOBRIDGE_PC] setting local description")
        try:
            await self.pc.setLocalDescription(answer)
        except Exception as e:
            print("[FATAL_EXCEPTION] setLocalDescription failed:", e)
            _tb.print_exc()
            raise
        print("[AUDIOBRIDGE_PC] local description set")

        for transceiver in self.pc.getTransceivers():
            print(
                "[TRANSCEIVER_FINAL]",
                "kind=", transceiver.kind,
                "direction=", transceiver.direction,
                "currentDirection=", transceiver.currentDirection,
            )

        # Step 4: wait for ICE gathering
        try:
            await asyncio.wait_for(self._wait_for_ice_gathering_complete(), timeout=5.0)
        except asyncio.TimeoutError:
            logger.warning("[AUDIOBRIDGE_PC] ICE gathering timeout — proceeding")

        sdp = self.pc.localDescription.sdp
        print("[AUDIOBRIDGE_PC] LOCAL SDP START")
        print(sdp)
        print("[AUDIOBRIDGE_PC] LOCAL SDP END")

        return {"type": self.pc.localDescription.type, "sdp": sdp}



    async def add_ice_candidate(self, candidate_info: dict):
        """Add a trickle ICE candidate received from Janus."""
        if not self.pc:
            logger.debug("Ignoring ICE candidate because PeerConnection is not initialized")
            return

        if candidate_info.get("completed"):
            logger.info("Remote ICE gathering completed.")
            return

        sdp_mid = candidate_info.get("sdpMid")
        sdp_mline_index = candidate_info.get("sdpMLineIndex")
        candidate_sdp = candidate_info.get("candidate")

        if candidate_sdp:
            try:
                candidate = candidate_from_sdp(candidate_sdp)
                candidate.sdpMid = sdp_mid
                candidate.sdpMLineIndex = sdp_mline_index
                await self.pc.addIceCandidate(candidate)
                logger.debug("Added remote ICE candidate: %s", candidate_sdp)
            except Exception as e:
                logger.error("Failed to add remote ICE candidate: %s", e)

    async def close(self):
        """Close the PeerConnection and stop all tracks/receivers."""
        logger.info("Closing RTCTransport...")
        if self._stats_task:
            self._stats_task.cancel()
            try:
                await self._stats_task
            except asyncio.CancelledError:
                pass
            self._stats_task = None

        for task in list(self._audio_reader_tasks):
            task.cancel()
        self._audio_reader_tasks.clear()

        for receiver in self.audio_receivers:
            await receiver.stop()
        self.audio_receivers.clear()

        if self.pc:
            await self.pc.close()
            self.pc = None
        self._audio_transceiver_added = False
        logger.info("RTCTransport closed.")

    async def _poll_stats(self):
        while True:
            try:
                await asyncio.sleep(2.0)
                if not self.pc:
                    return
                stats = await self.pc.getStats()
                for stat in stats.values():
                    if stat.type == "candidate-pair" and getattr(stat, "selected", False):
                        logger.warning(
                            "[ICE_SELECTED] state=%s bytesReceived=%s packetsReceived=%s bytesSent=%s packetsSent=%s",
                            getattr(stat, "state", None),
                            getattr(stat, "bytesReceived", 0),
                            getattr(stat, "packetsReceived", 0),
                            getattr(stat, "bytesSent", 0),
                            getattr(stat, "packetsSent", 0),
                        )
                    if stat.type in {"inbound-rtp", "remote-inbound-rtp"} and getattr(stat, "kind", "") == "audio":
                        logger.warning(
                            "[RTP_STATS] type=%s packetsReceived=%s bytesReceived=%s packetsLost=%s jitter=%s",
                            stat.type,
                            getattr(stat, "packetsReceived", 0),
                            getattr(stat, "bytesReceived", 0),
                            getattr(stat, "packetsLost", 0),
                            getattr(stat, "jitter", 0),
                        )
            except asyncio.CancelledError:
                return
            except Exception as exc:
                logger.error("Stats polling error: %s", exc)

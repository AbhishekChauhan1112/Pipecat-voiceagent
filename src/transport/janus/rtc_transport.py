import asyncio
import logging
import traceback

from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp

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
        self.initialize()

    def initialize(self):
        """Initialize a fresh PeerConnection if one is not active."""
        if self.pc and self.pc.connectionState != "closed":
            return
        self.pc = RTCPeerConnection()
        self.pc.addTransceiver("audio", direction="recvonly")
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
            print(
                f"[TRACK] "
                f"kind={track.kind} "
                f"id={track.id}"
            )
            logger.warning("[TRACK] kind=%s id=%s", track.kind, track.id)
            if track.kind == "audio":
                print("[TASK] creating task")
                task = asyncio.create_task(self._read_audio(track))
                self._audio_reader_tasks.add(task)
                task.add_done_callback(self._audio_reader_tasks.discard)
            else:
                logger.warning("[TRACK_IGNORED] kind=%s id=%s", track.kind, track.id)

    async def _poll_stats(self):
        while True:
            try:
                stats = await self.pc.getStats()
                for stat in stats.values():
                    if stat.type == "candidate-pair":
                        if getattr(stat, "selected", False):
                            print(
                                f"[ICE_SELECTED] "
                                f"state={stat.state} "
                                f"bytesReceived={getattr(stat, 'bytesReceived', 0)} "
                                f"packetsReceived={getattr(stat, 'packetsReceived', 0)} "
                                f"bytesSent={getattr(stat, 'bytesSent', 0)} "
                                f"packetsSent={getattr(stat, 'packetsSent', 0)}"
                            )
            except Exception:
                traceback.print_exc()
            await asyncio.sleep(2)

    async def _read_audio(self, track):
        print("[AUDIO] reader started")
        logger.warning("[AUDIO] reader started track=%s", track.id)
        frames = 0
        while True:
            try:
                frame = await track.recv()
                frames += 1
                print(
                    f"[AUDIO_FRAME] "
                    f"count={frames} "
                    f"pts={frame.pts} "
                    f"samples={frame.samples} "
                    f"rate={frame.sample_rate}"
                )
                logger.warning(
                    "[AUDIO_FRAME] count=%s pts=%s samples=%s rate=%s",
                    frames,
                    frame.pts,
                    frame.samples,
                    frame.sample_rate,
                )
                if self.media_bridge:
                    await self.media_bridge.enqueue_inbound_frame(frame)
            except Exception as e:
                logger.error("[AUDIO_ERROR] %s", e)
                traceback.print_exc()
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

    async def create_audio_only_answer_for_offer(self, sdp: str) -> dict:
        """Accept an incoming offer and create SDP answer with audio transceiver policy."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        logger.warning("[SDP_REMOTE_OFFER] %s", sdp)
        offer = RTCSessionDescription(sdp=sdp, type="offer")
        logger.info("Setting remote description (offer) for SIP incoming call...")
        logger.warning("[WEBRTC] setRemoteDescription START")
        print("[WEBRTC] setRemoteDescription START")
        await self.pc.setRemoteDescription(offer)
        print("[WEBRTC] setRemoteDescription DONE")
        logger.warning("[WEBRTC] setRemoteDescription DONE")

        logger.warning("[WEBRTC] createAnswer START")
        print("[WEBRTC] createAnswer START")
        answer = await self.pc.createAnswer()
        print("[WEBRTC] createAnswer DONE")
        logger.warning("[WEBRTC] createAnswer DONE")
        logger.warning("[WEBRTC] setLocalDescription START")
        print("[WEBRTC] setLocalDescription START")
        await self.pc.setLocalDescription(answer)
        print("[WEBRTC] setLocalDescription DONE")
        logger.warning("[WEBRTC] setLocalDescription DONE")

        try:
            await asyncio.wait_for(self._wait_for_ice_gathering_complete(), timeout=2.0)
        except asyncio.TimeoutError:
            logger.warning("Timeout waiting for ICE gathering while creating SIP answer")

        print("[WEBRTC] LOCAL SDP START")
        print(self.pc.localDescription.sdp)
        print("[WEBRTC] LOCAL SDP END")
        logger.warning("[SDP_LOCAL_ANSWER] %s", self.pc.localDescription.sdp)
        for t in self.pc.getTransceivers():
            print(
                f"[TRANSCEIVER] "
                f"kind={t.kind} "
                f"direction={t.direction} "
                f"currentDirection={t.currentDirection}"
            )
            logger.warning(
                "[TRANSCEIVER] kind=%s direction=%s currentDirection=%s",
                t.kind,
                t.direction,
                t.currentDirection,
            )
        logger.info("Created local SDP answer for SIP incoming call")
        return {"type": self.pc.localDescription.type, "sdp": self.pc.localDescription.sdp}

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

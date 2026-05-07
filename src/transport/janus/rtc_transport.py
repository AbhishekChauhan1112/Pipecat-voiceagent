import asyncio
import logging

from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.sdp import candidate_from_sdp

from .audio_tracks import AudioReceiver

logger = logging.getLogger(__name__)


class RTCTransport:
    def __init__(self, media_bridge=None):
        self.pc = None
        self.audio_receivers = []
        self.media_bridge = media_bridge
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
            logger.info("PeerConnection state is %s", self.pc.connectionState)
            if self.pc.connectionState == "failed":
                await self.pc.close()

        @self.pc.on("iceconnectionstatechange")
        async def on_iceconnectionstatechange():
            logger.info("ICE Connection state is %s", self.pc.iceConnectionState)

        @self.pc.on("icegatheringstatechange")
        async def on_icegatheringstatechange():
            logger.info("ICE Gathering state is %s", self.pc.iceGatheringState)

        @self.pc.on("track")
        def on_track(track):
            logger.info("Received remote track: %s (id: %s)", track.kind, track.id)
            if track.kind == "audio":
                if self.media_bridge:
                    self.media_bridge.start_inbound(track)
                else:
                    receiver = AudioReceiver(track)
                    receiver.start()
                    self.audio_receivers.append(receiver)

                    @track.on("ended")
                    async def on_ended():
                        logger.info("Remote track %s ended", track.id)
                        await receiver.stop()
                        if receiver in self.audio_receivers:
                            self.audio_receivers.remove(receiver)

    def add_track(self, track):
        """Add a local MediaStreamTrack to the PeerConnection."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        for sender in self.pc.getSenders():
            if sender.track is track:
                logger.debug("Track already added, skipping duplicate sender")
                return

        logger.info("Adding local track: %s", track.kind)
        self.pc.addTrack(track)

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
        """Accept an incoming offer and create an audio-only SDP answer."""
        if not self.pc:
            raise RuntimeError("PeerConnection not initialized")

        filtered_sdp = self._strip_video_mlines(sdp)
        offer = RTCSessionDescription(sdp=filtered_sdp, type="offer")
        logger.info("Setting remote description (offer) for SIP incoming call...")
        await self.pc.setRemoteDescription(offer)

        answer = await self.pc.createAnswer()
        await self.pc.setLocalDescription(answer)

        try:
            await asyncio.wait_for(self._wait_for_ice_gathering_complete(), timeout=2.0)
        except asyncio.TimeoutError:
            logger.warning("Timeout waiting for ICE gathering while creating SIP answer")

        logger.info("Created local SDP answer for SIP incoming call")
        return {"type": self.pc.localDescription.type, "sdp": self.pc.localDescription.sdp}

    def _strip_video_mlines(self, sdp: str) -> str:
        """Remove video m-sections from an SDP offer so we negotiate audio-only."""
        lines = sdp.splitlines()
        if not any(line.startswith("m=video") for line in lines):
            return sdp

        session_lines = []
        media_sections = []
        current = []

        for line in lines:
            if line.startswith("m="):
                if current:
                    media_sections.append(current)
                current = [line]
            else:
                if current:
                    current.append(line)
                else:
                    session_lines.append(line)
        if current:
            media_sections.append(current)

        removed_mids = set()
        kept_sections = []
        for section in media_sections:
            first = section[0]
            if first.startswith("m=video"):
                for l in section:
                    if l.startswith("a=mid:"):
                        removed_mids.add(l.split(":", 1)[1].strip())
                continue
            kept_sections.append(section)

        rewritten_session = []
        for l in session_lines:
            if l.startswith("a=group:BUNDLE"):
                parts = l.split()
                base = parts[:1]
                mids = [m for m in parts[1:] if m not in removed_mids]
                if mids:
                    rewritten_session.append(" ".join(base + mids))
                continue
            rewritten_session.append(l)

        out = rewritten_session[:]
        for sec in kept_sections:
            out.extend(sec)
        return "\r\n".join(out) + "\r\n"

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
        for receiver in self.audio_receivers:
            await receiver.stop()
        self.audio_receivers.clear()

        if self.pc:
            await self.pc.close()
            self.pc = None
        logger.info("RTCTransport closed.")

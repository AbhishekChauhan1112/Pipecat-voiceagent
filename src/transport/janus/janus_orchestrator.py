from __future__ import annotations

import logging

from . import config
from .audiobridge_manager import AudioBridgeManager
from .room_controller import RoomController
from .session_manager import JanusSessionManager
from .sip_bridge import SipBridge

logger = logging.getLogger(__name__)


class JanusOrchestrator:
    """High-level Janus orchestration for SIP call lifecycle and AudioBridge room control."""

    def __init__(self) -> None:
        self.session = JanusSessionManager()
        self.room_controller = RoomController()
        self.sip_bridge = SipBridge(self)
        self.audiobridge_manager = AudioBridgeManager(self)

        # compatibility aliases for existing code paths
        self.sip = self.sip_bridge
        self.audiobridge = self.audiobridge_manager

        self.sip_register_enabled = config.SIP_REGISTER_ENABLED
        self.sip_guest = config.SIP_GUEST_MODE
        self.sip_username = config.SIP_USERNAME
        self.sip_secret = config.SIP_SECRET
        self.sip_proxy = config.SIP_PROXY

    async def start(self) -> None:
        await self.session.connect()
        await self.session.create_session()
        await self.sip_bridge.attach()
        await self.audiobridge_manager.attach()
        await self.sip_bridge.register()

    async def stop(self) -> None:
        try:
            await self.audiobridge_manager.leave_room()
        except Exception:
            logger.exception("Error leaving AudioBridge during shutdown")

        try:
            await self.sip_bridge.hangup()
        except Exception:
            logger.exception("Error hanging up SIP during shutdown")

        await self.session.close()

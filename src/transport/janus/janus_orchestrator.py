from __future__ import annotations

import json
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
        self.session.raw_rx_callback = self.log_raw_rx
        self.room_controller = RoomController()
        self.sip_bridge = SipBridge(self)
        self.audiobridge_manager = AudioBridgeManager(self)

        # compatibility aliases for existing code paths
        self.sip = self.sip_bridge
        self.audiobridge = self.audiobridge_manager

        self.sip_register_enabled = config.SIP_REGISTER_ENABLED
        self.sip_guest = config.SIP_GUEST_MODE
        self.sip_username = config.SIP_USERNAME
        self.sip_authuser = config.SIP_AUTHUSER
        self.sip_secret = config.SIP_SECRET
        self.sip_proxy = config.SIP_PROXY

    async def send_plugin_message(self, handle_id: int, *, body: dict, jsep: dict | None = None) -> dict:
        payload = {
            "janus": "message",
            "session_id": self.session.session_id,
            "handle_id": handle_id,
            "body": body,
        }
        if jsep:
            payload["jsep"] = jsep

        logger.warning(f"[JANUS_RAW_TX] {payload}")
        return await self.session.send_plugin_message(handle_id, body=body, jsep=jsep)

    async def log_raw_rx(self, message: dict) -> None:
        logger.warning(f"[JANUS_RAW_RX] {message}")

    async def start(self) -> None:
        logger.warning("[ORCH_START] starting Janus orchestration")
        logger.warning(
            "[ORCH_CONFIG] %s",
            json.dumps(
                {
                    "ws_url": config.JANUS_WS_URL,
                    "room_id": config.ROOM_ID,
                    "sip_register_enabled": self.sip_register_enabled,
                    "sip_guest": self.sip_guest,
                    "sip_username": self.sip_username,
                    "sip_proxy": self.sip_proxy,
                },
                indent=2,
            ),
        )

        logger.warning("[ORCH_STEP] connect websocket")
        await self.session.connect()
        logger.warning("[ORCH_STEP_DONE] connect websocket")

        logger.warning("[ORCH_STEP] create session")
        await self.session.create_session()
        logger.warning("[ORCH_STEP_DONE] create session")

        logger.warning("[ORCH_STEP] attach SIP plugin")
        await self.sip_bridge.attach()
        logger.warning("[ORCH_STEP_DONE] attach SIP plugin")

        logger.warning("[ORCH_STEP] attach AudioBridge plugin")
        await self.audiobridge_manager.attach()
        logger.warning("[ORCH_STEP_DONE] attach AudioBridge plugin")

        logger.warning("[ORCH_STEP] SIP register")
        await self.sip_bridge.register()
        logger.warning("[ORCH_STEP_DONE] SIP register")

    async def stop(self) -> None:
        logger.warning("[ORCH_STOP] stopping Janus orchestration")
        try:
            logger.warning("[ORCH_STOP_STEP] AudioBridge leave")
            await self.audiobridge_manager.leave_room()
            logger.warning("[ORCH_STOP_STEP_DONE] AudioBridge leave")
        except Exception:
            logger.exception("[ORCH_STOP_ERROR] AudioBridge leave failed")

        try:
            logger.warning("[ORCH_STOP_STEP] SIP hangup")
            await self.sip_bridge.hangup()
            logger.warning("[ORCH_STOP_STEP_DONE] SIP hangup")
        except Exception:
            logger.exception("[ORCH_STOP_ERROR] SIP hangup failed")

        logger.warning("[ORCH_STOP_STEP] close session manager")
        await self.session.close()
        logger.warning("[ORCH_STOP_STEP_DONE] close session manager")

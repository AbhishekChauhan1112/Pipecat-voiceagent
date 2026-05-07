from __future__ import annotations

import asyncio
import logging
from typing import Any

from .janus_events import SipCallState

logger = logging.getLogger(__name__)


class SipBridge:
    """SIP plugin event bridge for call lifecycle -> room controller transitions."""

    def __init__(self, orchestrator: "JanusOrchestrator") -> None:
        self.orchestrator = orchestrator
        self.handle_id: int | None = None
        self.call_state = SipCallState()
        self._incoming_event = asyncio.Event()
        self._accepted_event = asyncio.Event()
        self._hangup_event = asyncio.Event()

    async def attach(self) -> int:
        self.handle_id = await self.orchestrator.session.attach_plugin("janus.plugin.sip")
        self.orchestrator.session.register_handle_handler(self.handle_id, self._on_plugin_event)
        return self.handle_id

    async def register(self) -> None:
        if not self.handle_id:
            raise RuntimeError("SIP handle not attached")

        if not self.orchestrator.sip_register_enabled:
            logger.info("SIP registration disabled; expecting externally routed SIP events")
            return

        body = {
            "request": "register",
            "type": "guest" if self.orchestrator.sip_guest else "register",
            "username": self.orchestrator.sip_username,
            "secret": self.orchestrator.sip_secret,
            "proxy": self.orchestrator.sip_proxy,
        }
        await self.orchestrator.session.send_plugin_message(self.handle_id, body=body)

    async def hangup(self) -> None:
        if not self.handle_id:
            return
        try:
            await self.orchestrator.session.send_plugin_message(self.handle_id, body={"request": "hangup"})
        except Exception:
            logger.exception("SIP hangup failed")

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        data = message.get("plugindata", {}).get("data", {})
        if data.get("sip") != "event":
            return

        call_id = message.get("call_id")
        result = data.get("result", {})
        event = result.get("event")

        if event == "incomingcall":
            self.call_state.call_id = call_id
            self.call_state.username = result.get("username")
            self.call_state.incoming = True
            self.call_state.accepted = False
            self.call_state.active = False
            self._incoming_event.set()
            logger.info("[SIP_CALL_RECEIVED] call_id=%s from=%s", call_id, self.call_state.username)
            await self.orchestrator.room_controller.on_sip_call_received(self.call_state)
            return

        if event == "accepted":
            self.call_state.call_id = call_id or self.call_state.call_id
            self.call_state.accepted = True
            self.call_state.active = True
            self._accepted_event.set()
            logger.info("[SIP_CALL_ACCEPTED] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_call_accepted(self.call_state)
            return

        if event == "media":
            self.call_state.active = True
            logger.info("[SIP_MEDIA_ACTIVE] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_media_active(self.call_state)
            return

        if event in {"hangup", "hangingup", "declining"}:
            self.call_state.active = False
            self.call_state.accepted = False
            self._hangup_event.set()
            logger.info("[CALL_ENDED] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_call_hangup(self.call_state)

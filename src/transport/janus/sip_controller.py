from __future__ import annotations

import asyncio
import logging
from typing import Any

from .janus_events import SipCallState

logger = logging.getLogger(__name__)


class SipController:
    """Controls Janus SIP plugin handle and call lifecycle events."""

    def __init__(self, orchestrator: "JanusOrchestrator") -> None:
        self.orchestrator = orchestrator
        self.handle_id: int | None = None
        self.call_state = SipCallState()
        self._incoming_event = asyncio.Event()
        self._accepted_event = asyncio.Event()
        self._hangup_event = asyncio.Event()

    async def attach(self) -> int:
        self.handle_id = await self.orchestrator.attach_plugin("janus.plugin.sip")
        self.orchestrator.register_handle_handler(self.handle_id, self._on_plugin_event)
        return self.handle_id

    async def register(self) -> None:
        if not self.handle_id:
            raise RuntimeError("SIP handle not attached")

        if not self.orchestrator.sip_register_enabled:
            logger.info("SIP registration disabled; waiting for externally routed incoming SIP events")
            return

        body = {
            "request": "register",
            "type": "guest" if self.orchestrator.sip_guest else "register",
            "username": self.orchestrator.sip_username,
            "secret": self.orchestrator.sip_secret,
            "proxy": self.orchestrator.sip_proxy,
        }

        await self.orchestrator.send_plugin_message(self.handle_id, body=body)
        logger.info("SIP register request submitted")

    async def hangup(self) -> None:
        if not self.handle_id:
            return
        try:
            await self.orchestrator.send_plugin_message(self.handle_id, body={"request": "hangup"})
        except Exception:
            logger.exception("SIP hangup request failed")

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        plugindata = message.get("plugindata", {}).get("data", {})
        if plugindata.get("sip") != "event":
            return

        call_id = message.get("call_id")
        result = plugindata.get("result", {})
        event = result.get("event")

        if event == "incomingcall":
            self.call_state.call_id = call_id
            self.call_state.username = result.get("username")
            self.call_state.incoming = True
            self.call_state.accepted = False
            self.call_state.active = False
            self.call_state.headers = result.get("headers", {})
            self._incoming_event.set()
            logger.info("[SIP_CALL_RECEIVED] call_id=%s from=%s", call_id, self.call_state.username)
            await self.orchestrator.room_manager.on_sip_call_received(self.call_state)
            return

        if event == "accepted":
            self.call_state.call_id = call_id or self.call_state.call_id
            self.call_state.accepted = True
            self.call_state.active = True
            self._accepted_event.set()
            logger.info("[SIP_CALL_ACCEPTED] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_manager.on_sip_call_accepted(self.call_state)
            return

        if event in {"hangup", "hangingup", "declining"}:
            code = result.get("code")
            reason = result.get("reason")
            logger.info("[SIP_CALL_HANGUP] call_id=%s code=%s reason=%s", self.call_state.call_id, code, reason)
            self.call_state.active = False
            self.call_state.accepted = False
            self._hangup_event.set()
            await self.orchestrator.room_manager.on_sip_call_hangup(self.call_state)
            return

        if event == "media":
            logger.debug("SIP media event: %s", result)

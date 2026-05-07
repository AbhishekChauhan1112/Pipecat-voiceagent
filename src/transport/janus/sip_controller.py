from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

from .janus_events import SipCallState

logger = logging.getLogger(__name__)


class SipController:
    """Legacy-compatible SIP controller with full diagnostics."""

    def __init__(self, orchestrator: "JanusOrchestrator") -> None:
        self.orchestrator = orchestrator
        self.handle_id: int | None = None
        self.call_state = SipCallState()
        self._incoming_event = asyncio.Event()
        self._accepted_event = asyncio.Event()
        self._hangup_event = asyncio.Event()

    async def attach(self) -> int:
        logger.warning("[SIP_CONTROLLER_ATTACH] attaching janus.plugin.sip")

        if hasattr(self.orchestrator, "session"):
            self.handle_id = await self.orchestrator.session.attach_plugin("janus.plugin.sip")
            self.orchestrator.session.register_handle_handler(self.handle_id, self._on_plugin_event)
        else:
            self.handle_id = await self.orchestrator.attach_plugin("janus.plugin.sip")
            self.orchestrator.register_handle_handler(self.handle_id, self._on_plugin_event)

        logger.warning("[SIP_CONTROLLER_ATTACH_DONE] handle_id=%s", self.handle_id)
        return self.handle_id

    async def register(self) -> None:
        if not self.handle_id:
            raise RuntimeError("SIP handle not attached")

        if not self.orchestrator.sip_register_enabled:
            logger.warning("[SIP_REGISTER] skipped because SIP_REGISTER_ENABLED=false")
            return

        logger.warning("[SIP_REGISTER] preparing SIP registration")

        payload = {
            "request": "register",
            "type": "guest" if self.orchestrator.sip_guest else "register",
            "username": self.orchestrator.sip_username,
            "secret": self.orchestrator.sip_secret,
            "proxy": self.orchestrator.sip_proxy,
        }

        logger.warning(f"[SIP_REGISTER_PAYLOAD] {payload}")

        if hasattr(self.orchestrator, "session"):
            response = await self.orchestrator.send_plugin_message(
                self.handle_id,
                body=payload
            )
        else:
            response = await self.orchestrator.send_plugin_message(self.handle_id, body=payload)

        logger.warning(f"[SIP_REGISTER_RESPONSE] {response}")

    async def hangup(self) -> None:
        if not self.handle_id:
            return

        logger.warning("[SIP_HANGUP] sending hangup request")
        try:
            if hasattr(self.orchestrator, "session"):
                response = await self.orchestrator.session.send_plugin_message(
                    self.handle_id,
                    body={"request": "hangup"},
                )
            else:
                response = await self.orchestrator.send_plugin_message(
                    self.handle_id,
                    body={"request": "hangup"},
                )
            logger.warning("[SIP_HANGUP_RESPONSE] %s", json.dumps(response, indent=2))
        except Exception:
            logger.exception("SIP hangup request failed")

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        logger.warning("[SIP_PLUGIN_EVENT_RAW] %s", json.dumps(message, indent=2))

        plugindata = message.get("plugindata", {}).get("data", {})
        if plugindata.get("sip") != "event":
            logger.warning("[SIP_PLUGIN_EVENT_IGNORED] sip field is %s", plugindata.get("sip"))
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
            logger.warning("[SIP_INCOMING_CALL] call_id=%s from=%s", call_id, self.call_state.username)

            room_handler = getattr(self.orchestrator, "room_controller", None) or getattr(self.orchestrator, "room_manager", None)
            if room_handler:
                await room_handler.on_sip_call_received(self.call_state)
            return

        if event == "accepted":
            self.call_state.call_id = call_id or self.call_state.call_id
            self.call_state.accepted = True
            self.call_state.active = True
            self._accepted_event.set()
            logger.warning("[SIP_ACCEPTED] call_id=%s", self.call_state.call_id)

            room_handler = getattr(self.orchestrator, "room_controller", None) or getattr(self.orchestrator, "room_manager", None)
            if room_handler:
                await room_handler.on_sip_call_accepted(self.call_state)
            return

        if event in {"hangup", "hangingup", "declining"}:
            code = result.get("code")
            reason = result.get("reason")
            self.call_state.active = False
            self.call_state.accepted = False
            self._hangup_event.set()
            logger.warning("[SIP_HANGUP] call_id=%s code=%s reason=%s", self.call_state.call_id, code, reason)

            room_handler = getattr(self.orchestrator, "room_controller", None) or getattr(self.orchestrator, "room_manager", None)
            if room_handler:
                await room_handler.on_sip_call_hangup(self.call_state)
            return

        if event == "media":
            logger.warning("[SIP_MEDIA] %s", json.dumps(result, indent=2))

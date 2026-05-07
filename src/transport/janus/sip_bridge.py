from __future__ import annotations

import asyncio
import json
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
        self._incoming_offer_handler = None

    def set_incoming_offer_handler(self, handler) -> None:
        self._incoming_offer_handler = handler

    async def attach(self) -> int:
        logger.warning("[SIP_ATTACH] attaching janus.plugin.sip")
        self.handle_id = await self.orchestrator.session.attach_plugin("janus.plugin.sip")
        logger.warning("[SIP_ATTACH_DONE] handle_id=%s", self.handle_id)

        self.orchestrator.session.register_handle_handler(self.handle_id, self._on_plugin_event)
        logger.warning("[SIP_HANDLER_REGISTERED] handle_id=%s", self.handle_id)
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
            "username": self.orchestrator.sip_username,
            "authuser": self.orchestrator.sip_authuser,
            "secret": self.orchestrator.sip_secret,
            "proxy": self.orchestrator.sip_proxy,
        }

        if self.orchestrator.sip_guest:
            payload["type"] = "guest"

        logger.warning(f"[SIP_REGISTER_PAYLOAD] {payload}")
        response = await self.orchestrator.send_plugin_message(
            self.handle_id,
            body=payload
        )
        logger.warning(f"[SIP_REGISTER_RESPONSE] {response}")

        data = response.get("plugindata", {}).get("data", {})
        result = data.get("result", {})
        event = result.get("event")

        if response.get("janus") == "error":
            logger.error("[SIP_REGISTER_FAILED] janus error response=%s", json.dumps(response, indent=2))
        elif event == "registered":
            logger.warning("[SIP_REGISTERED] username=%s", self.orchestrator.sip_username)
        else:
            logger.warning("[SIP_REGISTER_PENDING] waiting for async registered event")

    async def hangup(self) -> None:
        if not self.handle_id:
            return
        try:
            logger.warning("[SIP_HANGUP] sending hangup request")
            response = await self.orchestrator.session.send_plugin_message(
                self.handle_id,
                body={"request": "hangup"},
            )
            logger.warning("[SIP_HANGUP_RESPONSE] %s", json.dumps(response, indent=2))
        except Exception:
            logger.exception("SIP hangup failed")

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        logger.warning("[SIP_PLUGIN_EVENT_RAW] %s", json.dumps(message, indent=2))

        data = message.get("plugindata", {}).get("data", {})
        if data.get("sip") != "event":
            logger.warning("[SIP_PLUGIN_EVENT_IGNORED] sip field is %s", data.get("sip"))
            return

        call_id = message.get("call_id")
        result = data.get("result", {})
        event = result.get("event")

        logger.warning("[SIP_PLUGIN_EVENT] event=%s call_id=%s", event, call_id)

        if event == "incomingcall":
            self.call_state.call_id = call_id
            self.call_state.username = result.get("username")
            self.call_state.incoming = True
            self.call_state.accepted = False
            self.call_state.active = False
            self._incoming_event.set()
            logger.warning("[SIP_INCOMING_CALL] call_id=%s from=%s", call_id, self.call_state.username)

            jsep = message.get("jsep")
            if jsep and jsep.get("type") == "offer" and self._incoming_offer_handler:
                logger.warning("[SIP_INCOMINGCALL_OFFER] call_id=%s offer received, preparing accept", call_id)
                await self._incoming_offer_handler(call_id, jsep, message)

            await self.orchestrator.room_controller.on_sip_call_received(self.call_state)
            return

        if event == "accepted":
            self.call_state.call_id = call_id or self.call_state.call_id
            self.call_state.accepted = True
            self.call_state.active = True
            self._accepted_event.set()
            logger.warning("[SIP_ACCEPTED] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_call_accepted(self.call_state)
            return

        if event == "media":
            self.call_state.active = True
            logger.warning("[SIP_MEDIA] call_id=%s result=%s", self.call_state.call_id, json.dumps(result, indent=2))
            logger.warning("[SIP_MEDIA_ACTIVE] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_media_active(self.call_state)
            return

        if event in {"hangup", "hangingup", "declining"}:
            self.call_state.active = False
            self.call_state.accepted = False
            self._hangup_event.set()
            logger.warning("[SIP_HANGUP] call_id=%s result=%s", self.call_state.call_id, json.dumps(result, indent=2))
            logger.warning("[CALL_ENDED] call_id=%s", self.call_state.call_id)
            await self.orchestrator.room_controller.on_sip_call_hangup(self.call_state)
            return

        if event == "registered":
            logger.warning("[SIP_REGISTERED] async confirmation received")
            return

        if event == "registration_failed":
            logger.error("[SIP_REGISTER_FAILED] async failure result=%s", json.dumps(result, indent=2))
            return

        logger.warning("[SIP_EVENT_UNHANDLED] event=%s payload=%s", event, json.dumps(message, indent=2))

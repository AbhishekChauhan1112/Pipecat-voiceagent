from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

from . import config

logger = logging.getLogger(__name__)


class AudioBridgeManager:
    """AudioBridge handle manager for room join/leave/participant tracking."""

    def __init__(self, orchestrator: "JanusOrchestrator") -> None:
        self.orchestrator = orchestrator
        self.handle_id: int | None = None
        self.participant_id: int | None = None
        self._joined_event = asyncio.Event()
        self._left_event = asyncio.Event()

    async def attach(self) -> int:
        logger.warning("[AUDIOBRIDGE_ATTACH] attaching janus.plugin.audiobridge")
        self.handle_id = await self.orchestrator.session.attach_plugin("janus.plugin.audiobridge")
        logger.warning("[AUDIOBRIDGE_ATTACH_DONE] handle_id=%s", self.handle_id)

        self.orchestrator.session.register_handle_handler(self.handle_id, self._on_plugin_event)
        logger.warning("[AUDIOBRIDGE_HANDLER_REGISTERED] handle_id=%s", self.handle_id)
        return self.handle_id

    async def join_room(self, *, display: str, rtc=None) -> None:
        """Join the AudioBridge room, performing full WebRTC negotiation if rtc is provided."""
        if not self.handle_id:
            raise RuntimeError("AudioBridge handle not attached")

        payload_body = {
            "request": "join",
            "room": config.ROOM_ID,
            "pin": config.ROOM_PIN,
            "display": display,
        }
        if config.ROOM_PIN:
            payload_body["pin"] = config.ROOM_PIN

        self._rtc = rtc  # stash for use in _on_plugin_event
        self._joined_event.clear()

        # If rtc provided, create an offer now and include it in the join
        jsep_offer = None
        if rtc is not None:
            print("[AUDIOBRIDGE_JOIN] creating WebRTC offer for AudioBridge")
            jsep_offer = await rtc.create_offer()
            print("[AUDIOBRIDGE_JOIN] offer created:", jsep_offer.get("type"))

        logger.warning("[AUDIOBRIDGE_JOIN] sending join request body=%s", json.dumps(payload_body, indent=2))
        response = await self.orchestrator.session.send_plugin_message(
            self.handle_id,
            body=payload_body,
            jsep=jsep_offer,
        )
        logger.warning("[AUDIOBRIDGE_JOIN_RESPONSE] %s", json.dumps(response, indent=2))

        logger.warning("[AUDIOBRIDGE_JOIN_WAIT] waiting for async joined event")
        await asyncio.wait_for(self._joined_event.wait(), timeout=15.0)
        logger.warning("[AUDIOBRIDGE_JOINED] room=%s participant=%s", config.ROOM_ID, self.participant_id)

    async def leave_room(self) -> None:
        if not self.handle_id or not self._joined_event.is_set():
            logger.warning("[AUDIOBRIDGE_LEAVE_SKIP] handle=%s joined=%s", self.handle_id, self._joined_event.is_set())
            return

        self._left_event.clear()
        body = {"request": "leave", "room": config.ROOM_ID}

        try:
            logger.warning("[AUDIOBRIDGE_LEAVE] sending leave request body=%s", json.dumps(body, indent=2))
            response = await self.orchestrator.session.send_plugin_message(self.handle_id, body=body)
            logger.warning("[AUDIOBRIDGE_LEAVE_RESPONSE] %s", json.dumps(response, indent=2))

            logger.warning("[AUDIOBRIDGE_LEAVE_WAIT] waiting for async left event")
            await asyncio.wait_for(self._left_event.wait(), timeout=5.0)
            logger.warning("[AUDIOBRIDGE_LEFT] room=%s", config.ROOM_ID)
        except Exception:
            logger.exception("AudioBridge leave failed")
        finally:
            self._joined_event.clear()
            self.participant_id = None

    async def list_participants(self) -> list[dict[str, Any]]:
        if not self.handle_id:
            logger.warning("[AUDIOBRIDGE_PARTICIPANTS] no handle attached")
            return []

        body = {"request": "listparticipants", "room": config.ROOM_ID}
        logger.warning("[AUDIOBRIDGE_PARTICIPANTS_REQ] body=%s", json.dumps(body, indent=2))
        response = await self.orchestrator.session.send_plugin_message(self.handle_id, body=body)
        logger.warning("[AUDIOBRIDGE_PARTICIPANTS_RESP] %s", json.dumps(response, indent=2))

        data = response.get("plugindata", {}).get("data", {})
        participants = data.get("participants", [])
        valid = participants if isinstance(participants, list) else []
        logger.warning("[AUDIOBRIDGE_PARTICIPANTS] %s", json.dumps(valid, indent=2))
        return valid

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        logger.warning("[AUDIOBRIDGE_PLUGIN_EVENT_RAW] %s", json.dumps(message, indent=2))

        data = message.get("plugindata", {}).get("data", {})
        event_type = data.get("audiobridge")
        logger.warning("[AUDIOBRIDGE_PLUGIN_EVENT] event=%s", event_type)

        if event_type == "joined":
            self.participant_id = data.get("id")
            jsep = message.get("jsep")
            logger.warning("[AUDIOBRIDGE_JOINED] participant_id=%s jsep_type=%s", self.participant_id, jsep.get("type") if jsep else None)

            if jsep and jsep.get("type") == "offer" and self._rtc is not None:
                print("[AUDIOBRIDGE_JOIN] AudioBridge sent JSEP offer — performing WebRTC answer")
                try:
                    answer_jsep = await self._rtc.join_audiobridge(jsep["sdp"])
                    print("[AUDIOBRIDGE_JOIN] answer created, sending configure")
                    configure_body = {"request": "configure", "muted": False}
                    configure_resp = await self.orchestrator.session.send_plugin_message(
                        self.handle_id,
                        body=configure_body,
                        jsep=answer_jsep,
                    )
                    logger.warning("[AUDIOBRIDGE_CONFIGURE_RESPONSE] %s", json.dumps(configure_resp, indent=2))
                    print("[AUDIOBRIDGE_JOIN] configure sent")
                except Exception as e:
                    import traceback
                    print("[AUDIOBRIDGE_JOIN_ERROR]", repr(e))
                    traceback.print_exc()
            elif jsep:
                logger.warning("[AUDIOBRIDGE_JOIN] JSEP present but rtc not available — skipping WebRTC negotiation")

            self._joined_event.set()
            return

        if event_type == "left":
            self._left_event.set()
            logger.warning("[AUDIOBRIDGE_LEFT_EVENT] participant_id=%s", self.participant_id)
            await self.orchestrator.room_controller.on_room_empty()
            return

        if event_type == "event":
            participants = data.get("participants")
            if isinstance(participants, list):
                logger.warning("[AUDIOBRIDGE_PARTICIPANTS] %s", json.dumps(participants, indent=2))
                await self.orchestrator.room_controller.on_participants_update(participants)

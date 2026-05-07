from __future__ import annotations

import asyncio
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
        self.handle_id = await self.orchestrator.session.attach_plugin("janus.plugin.audiobridge")
        self.orchestrator.session.register_handle_handler(self.handle_id, self._on_plugin_event)
        return self.handle_id

    async def join_room(self, *, display: str) -> None:
        if not self.handle_id:
            raise RuntimeError("AudioBridge handle not attached")

        self._joined_event.clear()
        await self.orchestrator.session.send_plugin_message(
            self.handle_id,
            body={
                "request": "join",
                "room": config.ROOM_ID,
                "pin": config.ROOM_PIN,
                "display": display,
                "group": "default",
            },
        )
        await asyncio.wait_for(self._joined_event.wait(), timeout=10.0)
        logger.info("[AUDIOBRIDGE_JOIN] room=%s participant=%s", config.ROOM_ID, self.participant_id)

    async def leave_room(self) -> None:
        if not self.handle_id or not self._joined_event.is_set():
            return

        self._left_event.clear()
        try:
            await self.orchestrator.session.send_plugin_message(
                self.handle_id,
                body={"request": "leave", "room": config.ROOM_ID},
            )
            await asyncio.wait_for(self._left_event.wait(), timeout=5.0)
        except Exception:
            logger.exception("AudioBridge leave failed")
        finally:
            self._joined_event.clear()
            self.participant_id = None

    async def list_participants(self) -> list[dict[str, Any]]:
        if not self.handle_id:
            return []

        response = await self.orchestrator.session.send_plugin_message(
            self.handle_id,
            body={"request": "listparticipants", "room": config.ROOM_ID},
        )
        data = response.get("plugindata", {}).get("data", {})
        participants = data.get("participants", [])
        return participants if isinstance(participants, list) else []

    async def _on_plugin_event(self, message: dict[str, Any]) -> None:
        data = message.get("plugindata", {}).get("data", {})
        event_type = data.get("audiobridge")

        if event_type == "joined":
            self.participant_id = data.get("id")
            self._joined_event.set()
            return

        if event_type == "left":
            self._left_event.set()
            await self.orchestrator.room_controller.on_room_empty()
            return

        if event_type == "event":
            participants = data.get("participants")
            if isinstance(participants, list):
                await self.orchestrator.room_controller.on_participants_update(participants)

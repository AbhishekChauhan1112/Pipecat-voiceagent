from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Awaitable, Callable

from . import config
from .janus_events import RoomState, SipCallState

logger = logging.getLogger(__name__)


class RoomController:
    """Call-driven room state and Pipecat connect/disconnect coordination."""

    def __init__(self) -> None:
        self.state = RoomState(room_id=config.ROOM_ID)
        self._lock = asyncio.Lock()
        self._on_pipecat_connect: Callable[[], Awaitable[None]] | None = None
        self._on_pipecat_disconnect: Callable[[], Awaitable[None]] | None = None

    def set_callbacks(
        self,
        *,
        on_pipecat_connect: Callable[[], Awaitable[None]],
        on_pipecat_disconnect: Callable[[], Awaitable[None]],
    ) -> None:
        self._on_pipecat_connect = on_pipecat_connect
        self._on_pipecat_disconnect = on_pipecat_disconnect
        logger.warning("[ROOM_CALLBACKS_SET] connect=%s disconnect=%s", on_pipecat_connect.__qualname__, on_pipecat_disconnect.__qualname__)

    async def on_sip_call_received(self, call: SipCallState) -> None:
        logger.warning("[ROOM_EVENT] on_sip_call_received call_id=%s", call.call_id)
        async with self._lock:
            self.state.sip_present = True
            logger.warning("[SIP_CALL_RECEIVED] call_id=%s", call.call_id)

    async def on_sip_call_accepted(self, call: SipCallState) -> None:
        logger.warning("[ROOM_EVENT] on_sip_call_accepted call_id=%s", call.call_id)
        async with self._lock:
            self.state.sip_present = True
            logger.warning("[SIP_CALL_ACCEPTED] call_id=%s", call.call_id)

    async def on_sip_media_active(self, call: SipCallState) -> None:
        logger.warning("[ROOM_EVENT] on_sip_media_active call_id=%s", call.call_id)
        async with self._lock:
            self.state.sip_present = True

        if self._on_pipecat_connect:
            logger.warning("[PIPECAT_CONNECT] scheduling as background task room=%s", self.state.room_id)
            asyncio.create_task(self._run_connect())

    async def _run_connect(self) -> None:
        try:
            logger.warning("[PIPECAT_CONNECT_AWAIT] begin")
            await self._on_pipecat_connect()
            logger.warning("[PIPECAT_CONNECT_AWAIT] done")
            async with self._lock:
                self.state.pipecat_present = True
                logger.warning("[ROOM_ACTIVE] room=%s", self.state.room_id)
        except Exception as exc:
            logger.error("[PIPECAT_CONNECT_FAILED] %s", exc, exc_info=True)

    async def on_sip_call_hangup(self, call: SipCallState) -> None:
        logger.warning("[ROOM_EVENT] on_sip_call_hangup call_id=%s", call.call_id)
        async with self._lock:
            self.state.sip_present = False
            logger.warning("[CALL_ENDED] call_id=%s", call.call_id)

        if self._on_pipecat_disconnect:
            logger.warning("[PIPECAT_DISCONNECT] room=%s", self.state.room_id)
            logger.warning("[PIPECAT_DISCONNECT_AWAIT] begin")
            await self._on_pipecat_disconnect()
            logger.warning("[PIPECAT_DISCONNECT_AWAIT] done")
            async with self._lock:
                self.state.pipecat_present = False
                logger.warning("[ROOM_EMPTY] room=%s", self.state.room_id)

    async def on_participants_update(self, participants: list[dict]) -> None:
        logger.warning("[AUDIOBRIDGE_PARTICIPANTS] %s", json.dumps(participants, indent=2))
        async with self._lock:
            self.state.participants = participants

    async def on_room_empty(self) -> None:
        logger.warning("[ROOM_EVENT] on_room_empty")
        async with self._lock:
            self.state.participants = []
            self.state.sip_present = False
            logger.warning("[ROOM_EMPTY] room=%s", self.state.room_id)

        if self._on_pipecat_disconnect:
            logger.warning("[PIPECAT_DISCONNECT] room empty handler")
            logger.warning("[PIPECAT_DISCONNECT_AWAIT] begin")
            await self._on_pipecat_disconnect()
            logger.warning("[PIPECAT_DISCONNECT_AWAIT] done")
            async with self._lock:
                self.state.pipecat_present = False

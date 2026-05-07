from __future__ import annotations

import asyncio
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

    async def on_sip_call_received(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = True
            logger.info("[SIP_CALL_RECEIVED] call_id=%s", call.call_id)

    async def on_sip_call_accepted(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = True
            logger.info("[SIP_CALL_ACCEPTED] call_id=%s", call.call_id)

    async def on_sip_media_active(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = True

        if self._on_pipecat_connect:
            logger.info("[PIPECAT_CONNECT] room=%s", self.state.room_id)
            await self._on_pipecat_connect()
            async with self._lock:
                self.state.pipecat_present = True
                logger.info("[ROOM_ACTIVE] room=%s", self.state.room_id)

    async def on_sip_call_hangup(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = False
            logger.info("[CALL_ENDED] call_id=%s", call.call_id)

        if self._on_pipecat_disconnect:
            logger.info("[PIPECAT_DISCONNECT] room=%s", self.state.room_id)
            await self._on_pipecat_disconnect()
            async with self._lock:
                self.state.pipecat_present = False
                logger.info("[ROOM_EMPTY] room=%s", self.state.room_id)

    async def on_participants_update(self, participants: list[dict]) -> None:
        async with self._lock:
            self.state.participants = participants

    async def on_room_empty(self) -> None:
        async with self._lock:
            self.state.participants = []
            self.state.sip_present = False
            logger.info("[ROOM_EMPTY] room=%s", self.state.room_id)

        if self._on_pipecat_disconnect:
            await self._on_pipecat_disconnect()
            async with self._lock:
                self.state.pipecat_present = False

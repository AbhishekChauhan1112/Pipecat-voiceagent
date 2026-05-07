from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable

from . import config
from .janus_events import RoomState, SipCallState

logger = logging.getLogger(__name__)


class RoomManager:
    """Coordinates SIP call state and Pipecat media activation callbacks."""

    def __init__(self) -> None:
        self.state = RoomState(room_id=config.ROOM_ID)
        self._lock = asyncio.Lock()
        self._on_connect: Callable[[], Awaitable[None]] | None = None
        self._on_disconnect: Callable[[], Awaitable[None]] | None = None

    def set_callbacks(
        self,
        *,
        on_connect: Callable[[], Awaitable[None]],
        on_disconnect: Callable[[], Awaitable[None]],
    ) -> None:
        self._on_connect = on_connect
        self._on_disconnect = on_disconnect

    async def on_sip_call_received(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = True
            logger.info("[SIP_CALL_RECEIVED] call_id=%s", call.call_id)

    async def on_sip_call_accepted(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = True
            logger.info("[SIP_CALL_ACCEPTED] call_id=%s", call.call_id)

        if self._on_connect:
            logger.info("[PIPECAT_CONNECT] preparing WebRTC + pipeline")
            await self._on_connect()
            async with self._lock:
                self.state.pipecat_present = True
                logger.info("[ROOM_ACTIVE] room=%s", self.state.room_id)

    async def on_sip_call_hangup(self, call: SipCallState) -> None:
        async with self._lock:
            self.state.sip_present = False
            logger.info("[ROOM_EMPTY] SIP caller left, call_id=%s", call.call_id)

        if self._on_disconnect:
            logger.info("[PIPECAT_DISCONNECT] tearing down WebRTC + pipeline")
            await self._on_disconnect()
            async with self._lock:
                self.state.pipecat_present = False

    async def on_audiobridge_participants(self, participants: list[dict]) -> None:
        async with self._lock:
            self.state.participants = participants

    async def on_audiobridge_empty(self) -> None:
        async with self._lock:
            self.state.participants = []
            self.state.sip_present = False
            logger.info("[ROOM_EMPTY] AudioBridge participant list is empty")

        if self._on_disconnect:
            logger.info("[PIPECAT_DISCONNECT] room empty cleanup")
            await self._on_disconnect()
            async with self._lock:
                self.state.pipecat_present = False

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class JanusEventType(str, Enum):
    SIP = "sip"
    AUDIOBRIDGE = "audiobridge"
    WEBRTCUP = "webrtcup"
    MEDIA = "media"
    HANGUP = "hangup"
    TRICKLE = "trickle"
    DETACHED = "detached"
    UNKNOWN = "unknown"


@dataclass(slots=True)
class JanusEvent:
    event_type: JanusEventType
    sender: int | None
    transaction: str | None
    raw: dict[str, Any]


@dataclass(slots=True)
class SipCallState:
    call_id: str | None = None
    username: str | None = None
    incoming: bool = False
    accepted: bool = False
    active: bool = False
    headers: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RoomState:
    room_id: int
    sip_present: bool = False
    pipecat_present: bool = False
    participants: list[dict[str, Any]] = field(default_factory=list)

    @property
    def active(self) -> bool:
        return self.sip_present and self.pipecat_present

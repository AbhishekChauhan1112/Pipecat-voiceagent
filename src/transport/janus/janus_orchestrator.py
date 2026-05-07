from __future__ import annotations

import asyncio
import json
import logging
import random
import string
from collections.abc import Awaitable, Callable
from typing import Any

import websockets

from . import config
from .audiobridge_controller import AudioBridgeController
from .room_manager import RoomManager
from .sip_controller import SipController

logger = logging.getLogger(__name__)


def _txid(length: int = 12) -> str:
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class JanusOrchestrator:
    """Event-driven Janus control-plane orchestration for SIP + AudioBridge."""

    def __init__(self) -> None:
        self.ws = None
        self.session_id: int | None = None
        self.running = False

        self.transactions: dict[str, asyncio.Future] = {}
        self.handle_handlers: dict[int, Callable[[dict[str, Any]], Awaitable[None]]] = {}

        self.keepalive_task = None
        self.receive_task = None

        self.room_manager = RoomManager()
        self.sip = SipController(self)
        self.audiobridge = AudioBridgeController(self)

        self.sip_register_enabled = config.SIP_REGISTER_ENABLED
        self.sip_guest = config.SIP_GUEST_MODE
        self.sip_username = config.SIP_USERNAME
        self.sip_secret = config.SIP_SECRET
        self.sip_proxy = config.SIP_PROXY

    async def start(self) -> None:
        await self._connect()
        await self._create_session()
        await self.sip.attach()
        await self.audiobridge.attach()
        await self.sip.register()

    async def stop(self) -> None:
        self.running = False

        if self.keepalive_task:
            self.keepalive_task.cancel()
        if self.receive_task:
            self.receive_task.cancel()

        try:
            await self.audiobridge.leave_room()
        except Exception:
            logger.exception("Error leaving AudioBridge during shutdown")

        try:
            await self.sip.hangup()
        except Exception:
            logger.exception("Error hanging up SIP during shutdown")

        if self.ws:
            await self.ws.close()
            self.ws = None

    def register_handle_handler(
        self,
        handle_id: int,
        handler: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> None:
        self.handle_handlers[handle_id] = handler

    async def attach_plugin(self, plugin_name: str) -> int:
        response = await self._send_request(
            {
                "janus": "attach",
                "plugin": plugin_name,
                "session_id": self.session_id,
            }
        )
        if response.get("janus") != "success":
            raise RuntimeError(f"Failed to attach {plugin_name}: {response}")
        handle_id = response["data"]["id"]
        logger.info("Attached plugin=%s handle_id=%s", plugin_name, handle_id)
        return handle_id

    async def send_plugin_message(self, handle_id: int, *, body: dict, jsep: dict | None = None) -> dict:
        payload: dict[str, Any] = {
            "janus": "message",
            "session_id": self.session_id,
            "handle_id": handle_id,
            "body": body,
        }
        if jsep:
            payload["jsep"] = jsep

        response = await self._send_request(payload)

        # Janus often sends ack first for async plugin requests.
        if response.get("janus") == "ack":
            logger.debug("Received ack for handle=%s request=%s", handle_id, body.get("request"))
        return response

    async def _connect(self) -> None:
        logger.info("Connecting orchestrator to Janus at %s", config.JANUS_WS_URL)
        self.ws = await websockets.connect(config.JANUS_WS_URL, subprotocols=["janus-protocol"])
        self.running = True
        self.receive_task = asyncio.create_task(self._receive_loop())

    async def _create_session(self) -> None:
        response = await self._send_request({"janus": "create"})
        if response.get("janus") != "success":
            raise RuntimeError(f"Failed to create Janus session: {response}")

        self.session_id = response["data"]["id"]
        logger.info("Created Janus session: %s", self.session_id)
        self.keepalive_task = asyncio.create_task(self._keepalive_loop())

    async def _send_request(self, payload: dict[str, Any], timeout: float = 10.0) -> dict:
        if not self.ws:
            raise RuntimeError("Janus websocket is not connected")

        transaction = _txid()
        payload["transaction"] = transaction

        if self.session_id and "session_id" not in payload:
            payload["session_id"] = self.session_id

        fut = asyncio.get_event_loop().create_future()
        self.transactions[transaction] = fut

        await self.ws.send(json.dumps(payload))

        try:
            response = await asyncio.wait_for(fut, timeout=timeout)
            return response
        finally:
            self.transactions.pop(transaction, None)

    async def _receive_loop(self) -> None:
        try:
            async for raw in self.ws:
                msg = json.loads(raw)
                janus_type = msg.get("janus")
                transaction = msg.get("transaction")

                if transaction and transaction in self.transactions:
                    fut = self.transactions[transaction]
                    if not fut.done():
                        fut.set_result(msg)

                sender = msg.get("sender")
                if sender and sender in self.handle_handlers:
                    await self.handle_handlers[sender](msg)

                if janus_type == "hangup":
                    logger.info("Janus hangup event: %s", msg.get("reason"))
                elif janus_type == "detached":
                    logger.info("Janus detached handle: %s", sender)
                elif janus_type == "webrtcup":
                    logger.info("Janus WebRTC up for handle=%s", sender)
                elif janus_type == "media":
                    logger.debug(
                        "Janus media event handle=%s type=%s receiving=%s",
                        sender,
                        msg.get("type"),
                        msg.get("receiving"),
                    )
        except websockets.ConnectionClosed:
            logger.warning("Janus websocket closed")
        except asyncio.CancelledError:
            logger.debug("Orchestrator receive loop cancelled")
        except Exception:
            logger.exception("Janus receive loop error")

    async def _keepalive_loop(self) -> None:
        try:
            while self.running and self.ws and self.session_id:
                await asyncio.sleep(config.KEEPALIVE_INTERVAL)
                payload = {
                    "janus": "keepalive",
                    "session_id": self.session_id,
                    "transaction": _txid(),
                }
                await self.ws.send(json.dumps(payload))
        except asyncio.CancelledError:
            pass
        except Exception:
            logger.exception("Janus keepalive loop error")

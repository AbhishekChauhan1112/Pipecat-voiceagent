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

logger = logging.getLogger(__name__)


class JanusSessionManager:
    """Low-level Janus session transport with transaction correlation and event routing."""

    def __init__(self) -> None:
        self.ws = None
        self.session_id: int | None = None
        self.running = False

        self.transactions: dict[str, asyncio.Future] = {}
        self.handle_handlers: dict[int, Callable[[dict[str, Any]], Awaitable[None]]] = {}

        self.keepalive_task = None
        self.receive_task = None

    async def connect(self) -> None:
        logger.info("Connecting Janus session manager to %s", config.JANUS_WS_URL)
        self.ws = await websockets.connect(config.JANUS_WS_URL, subprotocols=["janus-protocol"])
        self.running = True
        self.receive_task = asyncio.create_task(self._receive_loop())

    async def create_session(self) -> int:
        response = await self.send_request({"janus": "create"})
        if response.get("janus") != "success":
            raise RuntimeError(f"Failed to create Janus session: {response}")

        self.session_id = response["data"]["id"]
        logger.info("Created Janus session id=%s", self.session_id)
        self.keepalive_task = asyncio.create_task(self._keepalive_loop())
        return self.session_id

    async def close(self) -> None:
        self.running = False
        if self.keepalive_task:
            self.keepalive_task.cancel()
        if self.receive_task:
            self.receive_task.cancel()
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
        response = await self.send_request(
            {
                "janus": "attach",
                "plugin": plugin_name,
                "session_id": self.session_id,
            }
        )
        if response.get("janus") != "success":
            raise RuntimeError(f"Failed to attach plugin={plugin_name}: {response}")

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

        response = await self.send_request(payload)
        if response.get("janus") == "ack":
            logger.debug("Ack for handle=%s request=%s", handle_id, body.get("request"))
        return response

    async def send_request(self, payload: dict[str, Any], timeout: float = 10.0) -> dict:
        if not self.ws:
            raise RuntimeError("Janus websocket not connected")

        txid = self._txid()
        payload["transaction"] = txid

        if self.session_id and "session_id" not in payload:
            payload["session_id"] = self.session_id

        fut = asyncio.get_event_loop().create_future()
        self.transactions[txid] = fut
        await self.ws.send(json.dumps(payload))

        try:
            return await asyncio.wait_for(fut, timeout=timeout)
        finally:
            self.transactions.pop(txid, None)

    async def _receive_loop(self) -> None:
        try:
            async for raw in self.ws:
                msg = json.loads(raw)
                tx = msg.get("transaction")
                janus_type = msg.get("janus")
                sender = msg.get("sender")

                if tx and tx in self.transactions:
                    fut = self.transactions[tx]
                    if not fut.done():
                        fut.set_result(msg)

                if sender and sender in self.handle_handlers:
                    await self.handle_handlers[sender](msg)

                if janus_type == "hangup":
                    logger.info("Janus hangup event: %s", msg.get("reason"))
                elif janus_type == "detached":
                    logger.info("Janus detached handle=%s", sender)
                elif janus_type == "media":
                    logger.debug(
                        "Janus media handle=%s type=%s receiving=%s",
                        sender,
                        msg.get("type"),
                        msg.get("receiving"),
                    )
        except websockets.ConnectionClosed:
            logger.warning("Janus websocket closed")
        except asyncio.CancelledError:
            logger.debug("Janus receive loop cancelled")
        except Exception:
            logger.exception("Janus receive loop error")

    async def _keepalive_loop(self) -> None:
        try:
            while self.running and self.ws and self.session_id:
                await asyncio.sleep(config.KEEPALIVE_INTERVAL)
                await self.ws.send(
                    json.dumps(
                        {
                            "janus": "keepalive",
                            "session_id": self.session_id,
                            "transaction": self._txid(),
                        }
                    )
                )
        except asyncio.CancelledError:
            pass
        except Exception:
            logger.exception("Keepalive loop error")

    @staticmethod
    def _txid(length: int = 12) -> str:
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

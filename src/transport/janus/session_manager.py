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
        self.raw_rx_callback = None

    async def connect(self) -> None:
        logger.warning("[WS_CONNECTING] url=%s", config.JANUS_WS_URL)
        self.ws = await websockets.connect(config.JANUS_WS_URL, subprotocols=["janus-protocol"])
        logger.warning("[WS_CONNECTED] url=%s", config.JANUS_WS_URL)

        self.running = True
        logger.warning("[WS_LISTENER_START] creating receive loop task")
        self.receive_task = asyncio.create_task(self._receive_loop())

    async def create_session(self) -> int:
        logger.warning("[SESSION_CREATE] sending create session request")
        response = await self.send_request({"janus": "create"})
        logger.warning("[SESSION_CREATE_RESPONSE] %s", json.dumps(response, indent=2))

        if response.get("janus") != "success":
            logger.error("[SESSION_CREATE_FAILED] %s", json.dumps(response, indent=2))
            raise RuntimeError(f"Failed to create Janus session: {response}")

        self.session_id = response["data"]["id"]
        logger.warning("[SESSION_CREATED] session_id=%s", self.session_id)

        logger.warning("[KEEPALIVE_START] creating keepalive loop task")
        self.keepalive_task = asyncio.create_task(self._keepalive_loop())
        return self.session_id

    async def close(self) -> None:
        logger.warning("[WS_CLOSE_BEGIN] shutting down Janus session manager")
        self.running = False

        if self.keepalive_task:
            logger.warning("[KEEPALIVE_STOP] cancelling keepalive task")
            self.keepalive_task.cancel()
        if self.receive_task:
            logger.warning("[WS_LISTENER_STOP] cancelling receive loop task")
            self.receive_task.cancel()

        if self.ws:
            logger.warning("[WS_DISCONNECTING] closing websocket")
            await self.ws.close()
            self.ws = None
            logger.warning("[WS_DISCONNECTED] websocket closed")

    def register_handle_handler(
        self,
        handle_id: int,
        handler: Callable[[dict[str, Any]], Awaitable[None]],
    ) -> None:
        logger.warning("[HANDLE_HANDLER_REGISTER] handle_id=%s handler=%s", handle_id, handler.__qualname__)
        self.handle_handlers[handle_id] = handler

    async def attach_plugin(self, plugin_name: str) -> int:
        payload = {
            "janus": "attach",
            "plugin": plugin_name,
            "session_id": self.session_id,
        }
        logger.warning("[PLUGIN_ATTACH] plugin=%s payload=%s", plugin_name, json.dumps(payload, indent=2))

        response = await self.send_request(payload)
        logger.warning("[PLUGIN_ATTACH_RESPONSE] plugin=%s response=%s", plugin_name, json.dumps(response, indent=2))

        if response.get("janus") != "success":
            logger.error("[PLUGIN_ATTACH_FAILED] plugin=%s response=%s", plugin_name, json.dumps(response, indent=2))
            raise RuntimeError(f"Failed to attach plugin={plugin_name}: {response}")

        handle_id = response["data"]["id"]
        logger.warning("[PLUGIN_ATTACHED] plugin=%s handle_id=%s", plugin_name, handle_id)
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

        logger.warning("[PLUGIN_MESSAGE_SEND] handle_id=%s request=%s", handle_id, body.get("request"))
        response = await self.send_request(payload)
        logger.warning("[PLUGIN_MESSAGE_RESPONSE] handle_id=%s response=%s", handle_id, json.dumps(response, indent=2))

        if response.get("janus") == "ack":
            logger.warning("[JANUS_ASYNC_ACK] handle_id=%s request=%s", handle_id, body.get("request"))

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

        logger.warning("[TX_CREATE] txid=%s payload=%s", txid, json.dumps(payload, indent=2))
        logger.warning("[WS_TX] txid=%s", txid)
        logger.warning("[JANUS_RAW_TX] %s", json.dumps(payload, indent=2))
        await self.ws.send(json.dumps(payload))

        logger.warning("[TX_WAIT] txid=%s timeout=%s", txid, timeout)
        try:
            response = await asyncio.wait_for(fut, timeout=timeout)
            logger.warning("[TX_RESOLVE] txid=%s response=%s", txid, json.dumps(response, indent=2))
            return response
        except asyncio.TimeoutError:
            logger.error("[TX_TIMEOUT] txid=%s pending=%s", txid, len(self.transactions))
            raise
        finally:
            self.transactions.pop(txid, None)

    async def _receive_loop(self) -> None:
        try:
            async for raw in self.ws:
                logger.warning("[WS_RX] bytes=%s", len(raw))
                try:
                    msg = json.loads(raw)
                except Exception:
                    logger.error("[JANUS_RAW_RX_PARSE_ERROR] raw=%s", raw)
                    raise

                logger.warning("[JANUS_RAW_RX] %s", json.dumps(msg, indent=2))
                if self.raw_rx_callback:
                    await self.raw_rx_callback(msg)

                tx = msg.get("transaction")
                janus_type = msg.get("janus")
                sender = msg.get("sender")

                if tx:
                    logger.warning("[TX_LOOKUP] txid=%s known=%s", tx, tx in self.transactions)

                if tx and tx in self.transactions:
                    fut = self.transactions[tx]
                    if not fut.done():
                        logger.warning("[TX_RESOLVE_DISPATCH] txid=%s", tx)
                        fut.set_result(msg)

                if sender:
                    logger.warning("[PLUGIN_EVENT_ROUTE] sender=%s handler_exists=%s", sender, sender in self.handle_handlers)

                if sender and sender in self.handle_handlers:
                    logger.warning("[PLUGIN_EVENT_DISPATCH] sender=%s janus=%s", sender, janus_type)
                    await self.handle_handlers[sender](msg)

                if janus_type == "ack":
                    logger.warning("[JANUS_ASYNC_ACK] sender=%s tx=%s", sender, tx)
                elif janus_type == "webrtcup":
                    logger.warning("[WEBRTC_UP] sender=%s", sender)
                elif janus_type == "media":
                    logger.warning("[WEBRTC_MEDIA_EVENT] sender=%s type=%s receiving=%s", sender, msg.get("type"), msg.get("receiving"))
                elif janus_type == "hangup":
                    logger.warning("[WEBRTC_HANGUP_EVENT] sender=%s reason=%s", sender, msg.get("reason"))
                elif janus_type == "detached":
                    logger.warning("[PLUGIN_DETACHED] sender=%s", sender)
        except websockets.ConnectionClosed as exc:
            logger.warning("[WS_DISCONNECTED] code=%s reason=%s", exc.code, exc.reason)
            logger.warning("[WS_RECONNECT_PENDING] no auto-reconnect implemented in manager")
        except asyncio.CancelledError:
            logger.warning("[WS_LISTENER_CANCELLED]")
        except Exception:
            logger.exception("[WS_LISTENER_ERROR]")

    async def _keepalive_loop(self) -> None:
        try:
            while self.running and self.ws and self.session_id:
                await asyncio.sleep(config.KEEPALIVE_INTERVAL)
                payload = {
                    "janus": "keepalive",
                    "session_id": self.session_id,
                    "transaction": self._txid(),
                }
                logger.warning("[KEEPALIVE_TX] %s", json.dumps(payload, indent=2))
                logger.warning("[JANUS_RAW_TX] %s", json.dumps(payload, indent=2))
                await self.ws.send(json.dumps(payload))
        except asyncio.CancelledError:
            logger.warning("[KEEPALIVE_CANCELLED]")
        except Exception:
            logger.exception("[KEEPALIVE_ERROR]")

    @staticmethod
    def _txid(length: int = 12) -> str:
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

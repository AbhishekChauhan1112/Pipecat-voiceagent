"""
Transport package for the Pipecat Voice Agent.

This package contains the network transport layer:
  - FastAPI application factory
  - WebSocket session routing
  - Health check and info endpoints

The transport layer is deliberately AI-free — it only handles
connection management and request routing.

Modules:
  server  – FastAPI app factory and WebSocket endpoint
"""

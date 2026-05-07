"""
Services package for the Pipecat Voice Agent.

Each module in this package is a thin factory layer responsible for
constructing a single AI provider service with production-ready settings.

Modules:
  stt_service  – Deepgram real-time WebSocket STT
  llm_service  – Groq streaming LLM + conversation context aggregators
  tts_service  – ElevenLabs WebSocket streaming TTS
"""

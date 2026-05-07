import os

# Janus Server Configuration
# If running this service on a different machine from Janus,
# set JANUS_WS_URL to the server's public address.
JANUS_WS_URL = os.getenv("JANUS_WS_URL", "ws://127.0.0.1:8188")
JANUS_REST_URL = os.getenv("JANUS_REST_URL", "http://127.0.0.1:8088/janus")

# Janus AudioBridge Room Configuration
ROOM_ID = int(os.getenv("ROOM_ID", "7007"))
ROOM_PIN = os.getenv("ROOM_PIN", "7007")

# WebRTC and Audio Configuration
AUDIO_SAMPLE_RATE = int(os.getenv("AUDIO_SAMPLE_RATE", "16000"))
AUDIO_CHANNELS = int(os.getenv("AUDIO_CHANNELS", "1"))
AUDIO_CODEC = os.getenv("AUDIO_CODEC", "opus")

# Display name for the WebRTC client in the AudioBridge room
DISPLAY_NAME = os.getenv("JANUS_DISPLAY_NAME", "pipecat-voiceagent")

# Keepalive interval in seconds
KEEPALIVE_INTERVAL = int(os.getenv("JANUS_KEEPALIVE_INTERVAL", "30"))

# Pipecat Telephony Voice Agent — FreeSWITCH + Linphone POC

## Architecture

```
Linphone (softphone)
      ↓ SIP  (calls extension 9000)
FreeSWITCH  (EC2 — SIP server)
      ↓ mod_audio_stream WebSocket
      ws://127.0.0.1:8765/ws   ← loopback, same machine
Pipecat Agent  (EC2 — this server)
      ↓ Deepgram STT → Groq LLM → ElevenLabs TTS
      ↓ binary PCM16 audio back
FreeSWITCH → RTP → Linphone  (caller hears the agent)
```

## Project Structure

```
Pipecat-voiceagent/
├── main.py
├── requirements.txt
├── .env.example
│
├── src/
│   ├── config.py
│   ├── logging_utils.py
│   ├── services/
│   │   ├── stt_service.py        Deepgram STT
│   │   ├── llm_service.py        Groq LLM + context memory
│   │   └── tts_service.py        ElevenLabs TTS
│   ├── pipeline/
│   │   └── agent_pipeline.py     Full call pipeline
│   └── transport/
│       ├── server.py             FastAPI WebSocket server
│       └── freeswitch_serializer.py  Binary PCM ↔ AudioRawFrame
│
├── config/
│   └── freeswitch/
│       ├── dialplan/01_ai_agent.xml          → copy to FreeSWITCH
│       └── autoload_configs/audio_stream.conf.xml
│
└── scripts/
    └── install_mod_audio_stream.sh   → run on EC2
```

---

## Step-by-Step Setup

### Step 1 — Install mod_audio_stream on EC2

`mod_audio_stream` is **not bundled** with FreeSWITCH. You must compile it:

```bash
# On your EC2 instance (Ubuntu)
git clone https://github.com/yourusername/Pipecat-voiceagent.git
cd Pipecat-voiceagent
sudo chmod +x scripts/install_mod_audio_stream.sh
sudo ./scripts/install_mod_audio_stream.sh
```

Verify it loaded:
```bash
fs_cli -x "module_exists mod_audio_stream"
# Should print: true
```

### Step 2 — Install FreeSWITCH dialplan

The install script does this automatically. To do it manually:

```bash
sudo cp config/freeswitch/dialplan/01_ai_agent.xml \
       /etc/freeswitch/dialplan/default/01_ai_agent.xml

sudo cp config/freeswitch/autoload_configs/audio_stream.conf.xml \
       /etc/freeswitch/autoload_configs/audio_stream.conf.xml

# Reload dialplan (no restart needed)
fs_cli -x "reloadxml"
```

### Step 3 — Configure Pipecat on EC2

```bash
# On EC2, inside the project directory
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Configure
cp .env.example .env
nano .env   # fill in DEEPGRAM_API_KEY, GROQ_API_KEY, ELEVENLABS_API_KEY
```

Key settings in `.env`:
```
HOST=127.0.0.1        # loopback only — FreeSWITCH is on same machine
PORT=8765
SAMPLE_RATE=16000     # must match dialplan audio_stream parameter
```

### Step 4 — Start the Agent

```bash
source .venv/bin/activate
python main.py
```

You should see:
```
╔══════════════════════════════════════════════╗
║   Pipecat Telephony Voice Agent  v1.0.0      ║
╚══════════════════════════════════════════════╝
  WebSocket    : ws://127.0.0.1:8765/ws  ← FreeSWITCH connects here
  Waiting for Linphone to call extension 9000 on FreeSWITCH…
```

### Step 5 — Configure Linphone

In Linphone (desktop or mobile):
1. **Add SIP account** → server = your EC2 IP, username = any local user (e.g. `1000`)
2. FreeSWITCH default users are in `/etc/freeswitch/directory/default/` (1000–1019)
3. Default password: `1234`
4. **Dial `9000`** — FreeSWITCH routes to the AI agent

---

## How It Works (Audio Flow)

```
1. Linphone dials 9000
2. FreeSWITCH answers (dialplan: application="answer")
3. FreeSWITCH opens WebSocket to ws://127.0.0.1:8765/ws
4. FreeSWITCH sends JSON handshake: {"uuid":"...", "rate":16000, ...}
5. FreeSWITCH streams binary PCM16 audio from Linphone mic
6. Pipecat FreeSwitchAudioSerializer deserializes bytes → AudioRawFrame
7. Silero VAD detects when you're speaking
8. Deepgram STT transcribes speech → text
9. Groq LLM generates response (streaming tokens)
10. ElevenLabs TTS synthesizes speech (streaming chunks)
11. Pipecat serializes audio → binary bytes → WebSocket → FreeSWITCH
12. FreeSWITCH plays audio back through RTP → Linphone speaker
```

### Barge-in (interruption)
If you speak while the agent is talking:
- Silero VAD detects your voice immediately
- Pipecat sends `CancelFrame` → ElevenLabs and Groq stop
- No more audio plays to you
- Your new speech starts a fresh STT → LLM → TTS cycle

---

## Troubleshooting

### mod_audio_stream not found
```bash
fs_cli -x "load mod_audio_stream"
# If "Failed": rebuild or check FS_MOD_DIR in install script
```

### No audio from agent
```bash
# Check Pipecat is running and listening
curl http://127.0.0.1:8765/health

# Check FreeSWITCH can reach the WebSocket
fs_cli -x "sofia status"
# Look at FreeSWITCH logs:
tail -f /var/log/freeswitch/freeswitch.log | grep audio_stream
```

### Agent doesn't respond / STT not working
```bash
# Run with DEBUG to see every frame
python main.py --log-level DEBUG
# Look for: "FreeSWITCH call connected" and Deepgram transcript lines
```

### Sample rate mismatch (choppy audio)
The log will warn: `FreeSWITCH sample rate mismatch`
Fix: make sure the dialplan `audio_stream` parameter and `.env SAMPLE_RATE` both say `16000`.

### Linphone can't register to FreeSWITCH
```bash
# Check FreeSWITCH SIP profile
fs_cli -x "sofia status profile internal"
# Default internal profile listens on port 5060
# Linphone: Server = <EC2_IP>:5060, User = 1000, Password = 1234
```

---

## Latency Guide

| Stage | Typical |
|-------|---------|
| FreeSWITCH → Pipecat (loopback) | < 1 ms |
| Silero VAD endpointing | 200–800 ms |
| Deepgram STT (final transcript) | 200–350 ms |
| Groq LLM first token | 150–300 ms |
| ElevenLabs TTS first chunk | 100–200 ms |
| **Total speech → first audio back** | **~650–1,650 ms** |

Lower latency tips:
- Use `DEEPGRAM_ENDPOINTING_MS=200` (faster but may cut off speech)
- Use `groq_model=llama-3.1-8b-instant` (2× faster, lower quality)
- Use `eleven_flash_v2_5` for TTS (lower latency model)

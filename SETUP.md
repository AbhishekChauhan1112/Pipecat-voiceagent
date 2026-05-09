# Pipecat Voice Agent — Complete Setup Guide

> FreeSWITCH is built from source and installed at `/usr/local/freeswitch/`

## How it works

```
Linphone (caller)
    ↓  dials 7007
FreeSWITCH
    ↓  dialplan matches ^7007$ → runs pipecat.lua
pipecat.lua
    ↓  uuid_audio_stream ... start ws://127.0.0.1:8765 stereo 16000
Python agent  (ws://127.0.0.1:8765)
    ↓  extracts caller audio (left channel) → VAD → Groq STT → Groq LLM → ElevenLabs TTS
    ↓  sends back: {"type":"streamAudio","data":{...base64 PCM...}}
pipecat.lua
    ↓  catches mod_audio_stream::play event → uuid_broadcast plays audio to caller
Caller hears the agent response
```

## Source-build directory layout

| Purpose            | Path                                              |
|--------------------|---------------------------------------------------|
| Binary / fs_cli    | `/usr/local/freeswitch/bin/`                      |
| Config / dialplan  | `/usr/local/freeswitch/conf/`                     |
| Lua scripts        | `/usr/local/freeswitch/scripts/`                  |
| Modules (.so)      | `/usr/local/freeswitch/mod/`                      |
| Logs               | `/usr/local/freeswitch/log/freeswitch.log`        |
| Sounds             | `/usr/local/freeswitch/sounds/`                   |

---

## Part 1 — Python Agent

### 1.1 Install dependencies

```bash
cd /usr/src/Pipecat-voiceagent
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 1.2 Configure .env

```bash
cp .env.example .env
nano .env
```

Minimum required values:

```env
# Required API keys
GROQ_API_KEY=gsk_...              # https://console.groq.com
ELEVENLABS_API_KEY=sk_...         # https://elevenlabs.io
DEEPGRAM_API_KEY=unused           # not used but required by config validator

# Agent
AGENT_NAME=Aria
SYSTEM_PROMPT=You are Aria, a helpful voice assistant answering a phone call. Be concise and natural.

# Audio — must match pipecat.lua RATE variable
SAMPLE_RATE=16000

# LLM
GROQ_MODEL=llama-3.3-70b-versatile
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=300

# TTS
ELEVENLABS_VOICE_ID=21m00Tcm4TlvDq8ikWAM
ELEVENLABS_MODEL=eleven_turbo_v2_5

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/agent.log
```

> Janus/SIP variables in .env are ignored by the websocket transport — leave them or remove them.

### 1.3 Run the agent

```bash
cd /usr/src/Pipecat-voiceagent
source .venv/bin/activate

# mod_audio_stream transport (default)
python main.py

# With debug logging (recommended while testing)
python main.py --log-level DEBUG

# Janus transport (optional)
python main.py --transport janus
```

Expected output:
```
║   Pipecat Telephony Voice Agent  v1.0.0      ║
  Transport    : websocket
  Listening on : ws://0.0.0.0:8765
  Waiting for FreeSWITCH mod_audio_stream connection…
```

### 1.4 Run as a systemd service (recommended for production)

```bash
nano /etc/systemd/system/pipecat-agent.service
```

```ini
[Unit]
Description=Pipecat Voice Agent
After=network.target

[Service]
User=root
WorkingDirectory=/usr/src/Pipecat-voiceagent
ExecStart=/usr/src/Pipecat-voiceagent/.venv/bin/python main.py --log-level INFO
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```bash
systemctl daemon-reload
systemctl enable pipecat-agent
systemctl start pipecat-agent
systemctl status pipecat-agent

# View live logs
journalctl -u pipecat-agent -f
```

---

## Part 2 — FreeSWITCH (source build)

### 2.1 Verify mod_audio_stream is loaded

```bash
/usr/local/freeswitch/bin/fs_cli -x "module_exists mod_audio_stream"
# Expected: true
```

If it returns `false`:
```bash
# Load for this session
/usr/local/freeswitch/bin/fs_cli -x "load mod_audio_stream"

# Make it permanent — edit:
nano /usr/local/freeswitch/conf/autoload_configs/modules.conf.xml
# Add inside <modules>:
#   <load module="mod_audio_stream"/>

# Then reload
/usr/local/freeswitch/bin/fs_cli -x "reloadxml"
```

### 2.2 Verify the dialplan (extension 7007)

```bash
# Find where your pipecat_agent dialplan is
grep -r "pipecat_agent\|7007" /usr/local/freeswitch/conf/dialplan/
```

It should have a condition matching `^7007$` that runs `pipecat.lua`:

```xml
<include>
  <context name="default">
    <extension name="pipecat_agent">
      <condition field="destination_number" expression="^7007$">
        <action application="answer"/>
        <action application="sleep"  data="500"/>
        <action application="lua"    data="pipecat.lua"/>
      </condition>
    </extension>
  </context>
</include>
```

> Change `^7007$` to whatever extension you want callers to dial.

### 2.3 Deploy pipecat.lua — CRITICAL STEP

The new `pipecat.lua` adds the `mod_audio_stream::play` event handler that plays TTS audio back to the caller. Without this the caller hears silence even if the Python agent is running.

```bash
# Find your scripts directory
/usr/local/freeswitch/bin/fs_cli -x "global_getvar script_dir"
# Typical source-build output: /usr/local/freeswitch/scripts

# Deploy
cp /usr/src/Pipecat-voiceagent/config/freeswitch/pipecat.lua \
   /usr/local/freeswitch/scripts/pipecat.lua

# Verify
cat /usr/local/freeswitch/scripts/pipecat.lua | grep uuid_broadcast
# Should print the uuid_broadcast line — confirms it's the new version
```

No FreeSWITCH restart needed — Lua scripts are read fresh on every call.

### 2.4 Reload dialplan

```bash
/usr/local/freeswitch/bin/fs_cli -x "reloadxml"
```

---

## Part 3 — Test

### Step 1: Start the Python agent

```bash
cd /usr/src/Pipecat-voiceagent
source .venv/bin/activate
python main.py --log-level DEBUG
```

### Step 2: Dial 7007 from Linphone

### Step 3: Watch Python agent logs — expected sequence

```
[WS] Connected: ('127.0.0.1', XXXXX)
[AFTER_TRANSPORT] FRAME TYPE: InputAudioRawFrame    ← caller audio flowing in
[AFTER_VAD] FRAME TYPE: UserStartedSpeakingFrame    ← VAD detected speech
[AFTER_STT] FRAME TYPE: TranscriptionFrame          ← Groq transcribed it
[AFTER_LLM] FRAME TYPE: TextFrame                   ← LLM generating response
[AFTER_TTS] FRAME TYPE: TTSAudioRawFrame             ← ElevenLabs synthesized audio
[WS_TX] streamAudio bytes=XXXXX                     ← sending audio to FreeSWITCH
```

### Step 4: Watch FreeSWITCH logs

```bash
tail -f /usr/local/freeswitch/log/freeswitch.log | grep pipecat
```

Expected:
```
[pipecat] session started: <uuid>
[pipecat] starting stream: uuid_audio_stream <uuid> start ws://127.0.0.1:8765 ...
[pipecat] WebSocket connected to Pipecat agent
[pipecat] playing TTS file: /tmp/XXXXXX.tmp.r8
```

---

## Part 4 — Troubleshooting

### Call connects but caller hears nothing

**Check 1 — Python agent listening?**
```bash
ss -tlnp | grep 8765
# Must show: LISTEN  0.0.0.0:8765
```

**Check 2 — pipecat.lua is the new version?**
```bash
grep -c "uuid_broadcast" /usr/local/freeswitch/scripts/pipecat.lua
# Must return 1 — if 0, you have the old version without TTS playback
```

**Check 3 — mod_audio_stream firing events?**
```bash
tail -f /usr/local/freeswitch/log/freeswitch.log | grep audio_stream
# Look for: adding bug   ← audio hook installed
#           resampling   ← audio is being sent to Python
```

### Call drops immediately (8–9 seconds)

Python agent is not running or port 8765 is not reachable from FreeSWITCH.
```bash
ss -tlnp | grep 8765          # check agent is up
# If not: start it with python main.py
```

### No transcription (agent never responds)

mod_audio_stream sends stereo audio; the Python agent takes the **left channel** (caller).
Look for `InputAudioRawFrame` in agent logs. If absent, the WebSocket is connected but no audio frames are arriving — check the `stereo` argument in pipecat.lua.

### Choppy TTS audio

- Lower `LLM_MAX_TOKENS=150` in `.env` for shorter, faster responses
- ElevenLabs `eleven_turbo_v2_5` is already the lowest-latency model

---

## Quick Reference

| Action | Command |
|--------|---------|
| Start agent | `python main.py` |
| Start agent (debug) | `python main.py --log-level DEBUG` |
| Start agent (Janus) | `python main.py --transport janus` |
| fs_cli | `/usr/local/freeswitch/bin/fs_cli` |
| Reload dialplan | `fs_cli -x "reloadxml"` |
| Check mod_audio_stream | `fs_cli -x "module_exists mod_audio_stream"` |
| FreeSWITCH config dir | `/usr/local/freeswitch/conf/` |
| Lua scripts dir | `/usr/local/freeswitch/scripts/` |
| FreeSWITCH log | `/usr/local/freeswitch/log/freeswitch.log` |
| Dial the agent | Extension **7007** from Linphone |

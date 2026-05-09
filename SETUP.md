# Pipecat Voice Agent — Complete Setup Guide

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

---

## Part 1 — Python Agent (on the same server as FreeSWITCH)

### 1.1 Install dependencies

```bash
cd /path/to/pipecat-voiceagent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 1.2 Configure .env

```bash
cp .env.example .env
nano .env
```

Fill in the required API keys:

```env
GROQ_API_KEY=gsk_...          # https://console.groq.com
ELEVENLABS_API_KEY=sk_...     # https://elevenlabs.io

# Leave these as-is for mod_audio_stream transport:
SAMPLE_RATE=16000
AUDIO_SAMPLE_RATE=16000
AUDIO_CHANNELS=1

# Agent personality
AGENT_NAME=Aria
SYSTEM_PROMPT=You are Aria, a helpful voice assistant answering a phone call. Be concise and natural.

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

> The Janus-specific variables (JANUS_WS_URL, ROOM_ID, etc.) are not needed for the
> mod_audio_stream transport but leaving them in does no harm.

### 1.3 Run the agent

```bash
# Default — mod_audio_stream WebSocket transport (what you want)
python main.py

# With debug logging (recommended while testing)
python main.py --log-level DEBUG

# Old Janus transport (optional, if you want to switch back)
python main.py --transport janus
```

You should see:
```
║   Pipecat Telephony Voice Agent  v1.0.0      ║
  Transport    : websocket
  Listening on : ws://0.0.0.0:8765
  Waiting for FreeSWITCH mod_audio_stream connection…
```

### 1.4 Run as a background service (optional)

Create `/etc/systemd/system/pipecat-agent.service`:

```ini
[Unit]
Description=Pipecat Voice Agent
After=network.target freeswitch.service

[Service]
User=www-data
WorkingDirectory=/path/to/pipecat-voiceagent
ExecStart=/path/to/pipecat-voiceagent/venv/bin/python main.py --log-level INFO
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable pipecat-agent
sudo systemctl start pipecat-agent
sudo systemctl status pipecat-agent
```

---

## Part 2 — FreeSWITCH

Your FreeSWITCH already has the right setup from the logs. Here is what must be in place.

### 2.1 Verify mod_audio_stream is loaded

```bash
fs_cli -x "module_exists mod_audio_stream"
# Expected output: true
```

If it returns `false`:
```bash
# Load it for this session
fs_cli -x "load mod_audio_stream"

# Make it permanent — add to /etc/freeswitch/autoload_configs/modules.conf.xml:
# <load module="mod_audio_stream"/>
```

### 2.2 Dialplan — already correct (extension 7007)

Your existing dialplan already has this extension. Verify it exists:

```bash
cat /etc/freeswitch/dialplan/default/pipecat_agent.xml
# or wherever you placed it
```

It should look like this (extension **7007** → runs **pipecat.lua**):

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

> Change `^7007$` to whatever extension number you want callers to dial.

### 2.3 Deploy pipecat.lua — THIS IS THE CRITICAL CHANGE

The old `pipecat.lua` starts streaming but does NOT handle the `mod_audio_stream::play`
event — that event is how the agent's TTS audio gets played back to the caller.

Copy the new script:

```bash
cp config/freeswitch/pipecat.lua /usr/share/freeswitch/scripts/pipecat.lua
# or:
cp config/freeswitch/pipecat.lua /etc/freeswitch/scripts/pipecat.lua
```

Find your scripts directory if unsure:
```bash
fs_cli -x "global_getvar script_dir"
```

The key part of the new pipecat.lua (event loop that plays TTS audio):

```lua
while session:ready() do
    session:getDigits(1, "#", 100)          -- short wait, keeps call alive
    local e = session:getEvent()
    if e then
        local subclass = e:getHeader("Event-Subclass") or ""
        if subclass == "mod_audio_stream::play" then
            local file = e:getHeader("file")
            if file then
                -- Play the TTS audio file back to the caller
                api:executeString("uuid_broadcast " .. uuid .. " " .. file .. " aleg")
            end
        end
    end
end
```

### 2.4 Reload FreeSWITCH dialplan

```bash
fs_cli -x "reloadxml"
```

No restart needed — Lua scripts are loaded fresh on each call.

---

## Part 3 — Test the setup

### Step 1: Start the Python agent

```bash
python main.py --log-level DEBUG
```

### Step 2: Make a test call

From Linphone (or any SIP phone registered to your FreeSWITCH):
- Dial **7007**

### Step 3: Watch the agent logs

You should see this sequence:

```
[WS] Connected: ('127.0.0.1', XXXXX)          ← FreeSWITCH connected
[AFTER_TRANSPORT] FRAME TYPE: InputAudioRawFrame   ← caller audio flowing in
[AFTER_VAD] FRAME TYPE: UserStartedSpeakingFrame   ← VAD detected speech
[AFTER_STT] FRAME TYPE: TranscriptionFrame         ← Groq transcribed it
[AFTER_LLM] FRAME TYPE: TextFrame                  ← LLM generating response
[AFTER_TTS] FRAME TYPE: TTSAudioRawFrame            ← ElevenLabs synthesized audio
[WS_TX] streamAudio bytes=XXXXX                    ← sending audio to FreeSWITCH
```

And in FreeSWITCH log (`/usr/local/freeswitch/log/freeswitch.log`):

```
[pipecat] WebSocket connected to Pipecat agent
[pipecat] playing TTS file: /tmp/XXXXXX.tmp.r8
```

---

## Part 4 — Troubleshooting

### Call connects but no audio from agent

**Check 1 — Is the Python agent running?**
```bash
ss -tlnp | grep 8765
# Should show: LISTEN 0.0.0.0:8765
```

**Check 2 — Is pipecat.lua the new version?**
The old script does not have the `mod_audio_stream::play` event handler.
Look for `uuid_broadcast` in the file — if it's missing, you have the old version.

**Check 3 — FreeSWITCH scripts directory**
```bash
fs_cli -x "global_getvar script_dir"
# Confirm pipecat.lua is in that exact directory
```

### Call drops immediately after connecting

The Python agent is not running or the WebSocket port 8765 is blocked by a firewall.
```bash
# Test WebSocket connectivity from FreeSWITCH server itself
python3 -c "import websocket; ws = websocket.create_connection('ws://127.0.0.1:8765'); print('OK')"
```

### Agent hears nothing / no transcription

mod_audio_stream sends **stereo** audio. The Python agent takes the **left channel** (caller's voice).
Check `[AFTER_TRANSPORT] FRAME TYPE: InputAudioRawFrame` appears in the agent logs — if it does,
audio is flowing. If not, check the stereo frame size with `--log-level DEBUG`.

### Choppy / delayed TTS audio

ElevenLabs `eleven_turbo_v2_5` has the lowest latency. If you want less delay:
- Lower `LLM_MAX_TOKENS` in `.env` (e.g., 150)
- Set `DEEPGRAM_ENDPOINTING_MS=200` for faster end-of-speech detection

### Check mod_audio_stream is receiving audio

In `fs_cli`:
```
sofia status
show channels
```

In FreeSWITCH log, look for:
```
[DEBUG] audio_streamer_glue.cpp resampling from XXXX to 16000
[DEBUG] mod_audio_stream.c adding bug.
```
If you see these, FreeSWITCH is streaming audio to the Python agent.

---

## Quick Reference

| Action | Command |
|--------|---------|
| Start agent | `python main.py` |
| Start agent (debug) | `python main.py --log-level DEBUG` |
| Start agent (Janus) | `python main.py --transport janus` |
| Reload FreeSWITCH dialplan | `fs_cli -x "reloadxml"` |
| Check mod_audio_stream loaded | `fs_cli -x "module_exists mod_audio_stream"` |
| View FreeSWITCH live log | `fs_cli -x "console loglevel debug"` then `fs_cli` |
| Dial the agent | Extension **7007** from Linphone |

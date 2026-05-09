--[[
  pipecat.lua — FreeSWITCH Lua script for Pipecat voice agent via mod_audio_stream

  Copy to: /usr/share/freeswitch/scripts/pipecat.lua
           (or wherever your FreeSWITCH scripts directory is)

  Dialplan trigger (dialplan/default/01_ai_agent.xml):
    <action application="answer"/>
    <action application="sleep"  data="500"/>
    <action application="lua"    data="pipecat.lua"/>

  What this script does:
    1. Answers the call and pauses 500 ms so RTP settles
    2. Subscribes to mod_audio_stream events on this session
    3. Starts streaming caller audio to ws://127.0.0.1:8765 (the Python agent)
    4. On every mod_audio_stream::play event (agent TTS response):
         - plays the temp audio file back to the caller
    5. Cleans up when the call ends
--]]

local WS_URL    = "ws://127.0.0.1:8765"
local STREAM    = "stereo"      -- left=caller, right=FS-leg; Python extracts left
local RATE      = "16000"       -- Hz — must match SAMPLE_RATE in ws_transport.py

-- ── helpers ──────────────────────────────────────────────────────────────────

local function log(level, msg)
    freeswitch.consoleLog(level, "[pipecat] " .. msg .. "\n")
end

-- ── main ─────────────────────────────────────────────────────────────────────

local uuid = session:get_uuid()
log("INFO", "session started: " .. uuid)

-- Subscribe to custom events fired by mod_audio_stream on this channel.
-- "CUSTOM" catches all Event-Subclass variants we need.
session:setHangupHook(function()
    log("INFO", "hangup hook fired for " .. uuid)
    return "true"
end)

-- Start audio streaming to the Pipecat WebSocket server
local api = freeswitch.API()
local cmd  = uuid .. " start " .. WS_URL .. " " .. STREAM .. " " .. RATE
log("INFO", "starting stream: uuid_audio_stream " .. cmd)
api:executeString("uuid_audio_stream " .. cmd)

-- Event loop: keep the call alive and play audio received from Pipecat
-- mod_audio_stream fires mod_audio_stream::play with a "file" header that
-- points to a temp PCM/WAV file written by mod_audio_stream.
log("INFO", "entering event loop")

while session:ready() do
    -- getDigits with short timeout lets us poll for events without blocking
    session:getDigits(1, "#", 100)

    -- Check for a pending custom event on this session
    local e = session:getEvent()
    if e then
        local subclass = e:getHeader("Event-Subclass") or ""
        if subclass == "mod_audio_stream::play" then
            local file = e:getHeader("file")
            if file then
                log("INFO", "playing TTS file: " .. file)
                -- uuid_broadcast plays the file on the A-leg (caller side)
                api:executeString("uuid_broadcast " .. uuid .. " " .. file .. " aleg")
            end
        elseif subclass == "mod_audio_stream::connect" then
            log("INFO", "WebSocket connected to Pipecat agent")
        elseif subclass == "mod_audio_stream::disconnect" then
            log("WARNING", "WebSocket disconnected from Pipecat agent")
        elseif subclass == "mod_audio_stream::error" then
            local msg = e:getHeader("message") or "unknown"
            log("ERR", "mod_audio_stream error: " .. msg)
        end
    end
end

-- ── cleanup ───────────────────────────────────────────────────────────────────
log("INFO", "call ended — stopping stream")
api:executeString("uuid_audio_stream " .. uuid .. " stop")
log("INFO", "done")

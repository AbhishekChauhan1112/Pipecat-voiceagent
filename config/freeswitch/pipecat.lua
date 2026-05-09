--[[
  pipecat.lua — FreeSWITCH Lua script for Pipecat voice agent via mod_audio_stream

  Copy to: /usr/local/freeswitch/scripts/pipecat.lua

  Dialplan trigger (dialplan/default/7007.xml):
    <action application="answer"/>
    <action application="sleep"  data="500"/>
    <action application="lua"    data="pipecat.lua"/>

  What this script does:
    1. Answers the call and pauses 500 ms so RTP settles
    2. Starts streaming caller audio to ws://127.0.0.1:8765 (the Python agent)
    3. On every mod_audio_stream::play event (agent TTS response):
         - plays the temp audio file back to the caller
    4. Cleans up when the call ends
--]]

local WS_URL = "ws://127.0.0.1:8765"
local STREAM  = "stereo"   -- left=caller, right=FS-leg; Python extracts left
local RATE    = "16000"    -- Hz — must match SAMPLE_RATE in ws_transport.py

-- ── helpers ──────────────────────────────────────────────────────────────────

local function log(level, msg)
    freeswitch.consoleLog(level, "[pipecat] " .. msg .. "\n")
end

-- ── main ─────────────────────────────────────────────────────────────────────

local uuid = session:get_uuid()
log("INFO", "session started: " .. uuid)

function onHangup(s, status, arg)
    log("INFO", "hangup hook fired for " .. uuid)
end
session:setHangupHook("onHangup")

-- Start audio streaming to the Pipecat WebSocket server
local api = freeswitch.API()
local cmd  = uuid .. " start " .. WS_URL .. " " .. STREAM .. " " .. RATE
log("INFO", "starting stream: uuid_audio_stream " .. cmd)
api:executeString("uuid_audio_stream " .. cmd)

-- Subscribe to CUSTOM events so we can catch mod_audio_stream::play.
-- freeswitch.EventConsumer is the correct Lua API — session:getEvent() does not exist.
local ec = freeswitch.EventConsumer("CUSTOM")

log("INFO", "entering event loop")

while session:ready() do
    -- pop(1, 100) = blocking pop with 100 ms timeout; keeps loop responsive to hangup
    local e = ec:pop(1, 100)
    if e then
        local subclass  = e:getHeader("Event-Subclass") or ""
        local evt_uuid  = e:getHeader("Unique-ID")      or ""

        -- Only handle events belonging to this session
        if evt_uuid == uuid then
            if subclass == "mod_audio_stream::play" then
                local file = e:getHeader("file")
                if file then
                    log("INFO", "playing TTS file: " .. file)
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
end

-- ── cleanup ───────────────────────────────────────────────────────────────────
log("INFO", "call ended — stopping stream")
api:executeString("uuid_audio_stream " .. uuid .. " stop")
log("INFO", "done")

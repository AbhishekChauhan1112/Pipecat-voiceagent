#!/usr/bin/env bash
# =============================================================================
# install_mod_audio_stream.sh
# Compiles and installs FreeSWITCH mod_audio_stream on Ubuntu 22.04 / 20.04
#
# Run as root (or with sudo) on your EC2 instance:
#   chmod +x install_mod_audio_stream.sh
#   sudo ./install_mod_audio_stream.sh
#
# mod_audio_stream repo: https://github.com/nicla-ai/freeswitch-mod-audio-stream
# (forked from briankwest/mod_audio_stream with active maintenance)
# =============================================================================

set -euo pipefail

# ── Colour helpers ────────────────────────────────────────────────────────────
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'
info()  { echo -e "${GREEN}[INFO]${NC}  $*"; }
warn()  { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error() { echo -e "${RED}[ERROR]${NC} $*"; exit 1; }

# ── Detect FreeSWITCH installation ───────────────────────────────────────────
FS_INCLUDE_DIR=""
for d in /usr/include/freeswitch /usr/local/include/freeswitch; do
  if [ -f "$d/switch.h" ]; then
    FS_INCLUDE_DIR="$d"
    break
  fi
done
[ -z "$FS_INCLUDE_DIR" ] && error "FreeSWITCH headers not found. Install freeswitch-dev first:
  apt-get install -y freeswitch-dev"

FS_MOD_DIR=""
for d in /usr/lib/freeswitch/mod /usr/local/lib/freeswitch/mod; do
  if [ -d "$d" ]; then
    FS_MOD_DIR="$d"
    break
  fi
done
[ -z "$FS_MOD_DIR" ] && error "FreeSWITCH modules directory not found."

info "FreeSWITCH headers: $FS_INCLUDE_DIR"
info "FreeSWITCH modules: $FS_MOD_DIR"

# ── Install build dependencies ────────────────────────────────────────────────
info "Installing build dependencies..."
apt-get update -qq
apt-get install -y --no-install-recommends \
  build-essential \
  git \
  cmake \
  pkg-config \
  libssl-dev \
  zlib1g-dev \
  freeswitch-dev 2>/dev/null || true

# ── Clone / update mod_audio_stream ──────────────────────────────────────────
REPO_DIR="/tmp/freeswitch-mod-audio-stream"
if [ -d "$REPO_DIR" ]; then
  info "Updating existing repo..."
  git -C "$REPO_DIR" pull --quiet
else
  info "Cloning mod_audio_stream..."
  git clone --depth 1 \
    https://github.com/nicla-ai/freeswitch-mod-audio-stream.git \
    "$REPO_DIR"
fi

cd "$REPO_DIR"

# ── Build ─────────────────────────────────────────────────────────────────────
info "Compiling mod_audio_stream..."
mkdir -p build && cd build
cmake .. \
  -DCMAKE_BUILD_TYPE=Release \
  -DFS_INCLUDE_DIR="$FS_INCLUDE_DIR" \
  2>&1 | tail -5

make -j"$(nproc)" 2>&1 | tail -10

# ── Install ───────────────────────────────────────────────────────────────────
SO_FILE="$(find . -name 'mod_audio_stream.so' | head -1)"
[ -z "$SO_FILE" ] && error "Build failed — mod_audio_stream.so not found."

info "Installing $SO_FILE → $FS_MOD_DIR/"
cp "$SO_FILE" "$FS_MOD_DIR/mod_audio_stream.so"
chmod 755 "$FS_MOD_DIR/mod_audio_stream.so"

# ── Enable in modules.conf.xml ────────────────────────────────────────────────
MODULES_CONF=""
for f in /etc/freeswitch/autoload_configs/modules.conf.xml \
          /usr/local/etc/freeswitch/autoload_configs/modules.conf.xml; do
  [ -f "$f" ] && MODULES_CONF="$f" && break
done

if [ -n "$MODULES_CONF" ]; then
  if grep -q "mod_audio_stream" "$MODULES_CONF"; then
    info "mod_audio_stream already in $MODULES_CONF"
  else
    info "Adding mod_audio_stream to $MODULES_CONF..."
    # Insert before </modules>
    sed -i 's|</modules>|    <load module="mod_audio_stream"/>\n</modules>|' "$MODULES_CONF"
    info "Added successfully."
  fi
else
  warn "Could not find modules.conf.xml. Add manually:"
  warn '  <load module="mod_audio_stream"/>'
fi

# ── Copy config file ──────────────────────────────────────────────────────────
FS_CONF_DIR=""
for d in /etc/freeswitch /usr/local/etc/freeswitch; do
  [ -d "$d/autoload_configs" ] && FS_CONF_DIR="$d" && break
done

AGENT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
CONF_SRC="$AGENT_DIR/config/freeswitch/autoload_configs/audio_stream.conf.xml"

if [ -f "$CONF_SRC" ] && [ -n "$FS_CONF_DIR" ]; then
  info "Installing audio_stream.conf.xml → $FS_CONF_DIR/autoload_configs/"
  cp "$CONF_SRC" "$FS_CONF_DIR/autoload_configs/audio_stream.conf.xml"
fi

# ── Install dialplan ──────────────────────────────────────────────────────────
DIALPLAN_SRC="$AGENT_DIR/config/freeswitch/dialplan/01_ai_agent.xml"
DIALPLAN_DST=""
for d in /etc/freeswitch/dialplan/default \
          /usr/local/etc/freeswitch/dialplan/default; do
  [ -d "$d" ] && DIALPLAN_DST="$d" && break
done

if [ -f "$DIALPLAN_SRC" ] && [ -n "$DIALPLAN_DST" ]; then
  info "Installing dialplan → $DIALPLAN_DST/01_ai_agent.xml"
  cp "$DIALPLAN_SRC" "$DIALPLAN_DST/01_ai_agent.xml"
fi

# ── Reload FreeSWITCH ─────────────────────────────────────────────────────────
info "Reloading FreeSWITCH modules..."
if command -v fs_cli &>/dev/null; then
  fs_cli -x "load mod_audio_stream" && info "mod_audio_stream loaded!" \
    || warn "FreeSWITCH reload failed — try: fs_cli -x 'reload mod_audio_stream'"
  fs_cli -x "reloadxml" && info "Dialplan reloaded."
else
  warn "fs_cli not found. Reload manually:"
  warn "  fs_cli -x 'load mod_audio_stream'"
  warn "  fs_cli -x 'reloadxml'"
fi

# ── Verify ────────────────────────────────────────────────────────────────────
echo ""
info "════════════════════════════════════════════════════"
info "  mod_audio_stream installation complete!"
info "  Verify with:  fs_cli -x 'module_exists mod_audio_stream'"
info ""
info "  Next steps:"
info "  1. Start Pipecat:    python main.py"
info "  2. Call ext 9000 from Linphone"
info "════════════════════════════════════════════════════"

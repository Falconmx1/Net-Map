#!/usr/bin/env bash
# Empaquetado de Net-Map para macOS (binario standalone con PyInstaller).
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

echo "[Net-Map] Instalando dependencias de build..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt pyinstaller

echo "[Net-Map] Generando binario para macOS..."
pyinstaller \
  --onefile \
  --name netmap \
  --paths "$ROOT_DIR" \
  --hidden-import scapy \
  src/cli/main.py

echo "[Net-Map] Generando app GUI para macOS..."
pyinstaller \
  --onefile \
  --windowed \
  --name netmap-gui \
  --paths "$ROOT_DIR" \
  --hidden-import scapy \
  src/gui/app.py

echo "[Net-Map] Artefactos generados en dist/"

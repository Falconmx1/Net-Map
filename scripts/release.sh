#!/usr/bin/env bash
# Construye wheel + sdist y valida el paquete.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[Net-Map] Instalando herramientas de build..."
python3 -m pip install --upgrade pip build twine

echo "[Net-Map] Construyendo wheel y sdist..."
python3 -m build

echo "[Net-Map] Validando paquete..."
python3 -m twine check dist/*

echo "[Net-Map] Listo. Artefactos en dist/"

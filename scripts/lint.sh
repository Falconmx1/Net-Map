#!/usr/bin/env bash
# Lint y verificación de sintaxis.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[Net-Map] Verificando sintaxis Python..."
python3 -m compileall -q src tests

echo "[Net-Map] Ejecutando pruebas..."
python3 -m unittest discover -s tests -v

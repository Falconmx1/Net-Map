# Empaquetado Windows

## Requisitos

- Python 3.9+
- Npcap instalado (https://npcap.com) para paquetes IP sin procesar.

## Generar binarios

```powershell
powershell -ExecutionPolicy Bypass -File packaging\windows\build.ps1
powershell -ExecutionPolicy Bypass -File packaging\windows\build-gui.ps1

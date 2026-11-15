# Empaquetado de Net-Map para Windows (binario standalone con PyInstaller).
$ErrorActionPreference = "Stop"

$RootDir = Resolve-Path "$PSScriptRoot\..\.."
Set-Location $RootDir

Write-Host "[Net-Map] Instalando dependencias de build..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pyinstaller

Write-Host "[Net-Map] Generando binario para Windows..."
pyinstaller `
  --onefile `
  --name netmap `
  --paths "$RootDir" `
  --hidden-import scapy `
  src/cli/main.py

Write-Host "[Net-Map] Binario generado en dist\netmap.exe"

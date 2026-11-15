# Empaquetado de la GUI de Net-Map para Windows.
$ErrorActionPreference = "Stop"

$RootDir = Resolve-Path "$PSScriptRoot\..\.."
Set-Location $RootDir

python -m pip install --upgrade pip
python -m pip install -r requirements.txt pyinstaller

pyinstaller `
  --onefile `
  --windowed `
  --name netmap-gui `
  --paths "$RootDir" `
  --hidden-import scapy `
  src/gui/app.py

Write-Host "[Net-Map] GUI generada en dist\netmap-gui.exe"

# Net-Map

Herramienta de código abierto para **descubrimiento de redes** y **auditoría de seguridad**. Usa paquetes IP sin procesar para identificar hosts, servicios (nombre y versión), sistemas operativos y firewalls. Útil también para **inventario de red**, **cronogramas de actualización** y **monitorización de uptime**.

## Características

- Descubrimiento de hosts y escaneo de puertos TCP/UDP.
- Detección de servicios, versiones, SO y filtros/firewalls.
- Escaneo rápido de redes grandes o de hosts individuales.
- Multiplataforma: Linux, Windows, macOS y más.
- CLI y GUI con visor de resultados.
- Componentes: `netmap`, `netmap-gui`, `netcat-map`, `netdiff`, `netping`, `netmap-inventory`.

## Inicio rápido
netmap -v -A targethost

## Estructura
src/ Motor, CLI, GUI, paquetes, diff, inventario
docs/ Documentación
tests/ Pruebas
scripts/ Utilidades
packaging/ Empaquetado por plataforma

## Documentación

- [Arquitectura](docs/arquitectura.md)
- [Uso de CLI](docs/uso-cli.md)
- [Uso de GUI](docs/uso-gui.md)
- [Técnicas de escaneo](docs/tecnicas-escaneo.md)
- [Inventario y uptime](docs/inventario-y-uptime.md)

## Uso responsable

Escanea **solo** redes propias o con autorización explícita. Reporta vulnerabilidades según `SECURITY.md`.

## Licencia

GPL-3.0. Ver `LICENSE`.

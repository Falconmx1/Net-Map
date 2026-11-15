# Arquitectura de Net-Map

## 1. Visión general

Net-Map es una herramienta de código abierto para el descubrimiento de redes y la
auditoría de seguridad. Utiliza paquetes IP sin procesar de formas innovadoras para
determinar qué hosts están disponibles, qué servicios ofrecen, qué sistemas operativos
ejecutan, qué filtros de paquetes/firewalls están en uso y docenas de otras
características. Está diseñada para escanear rápidamente redes grandes, pero funciona
igual de bien con hosts individuales.

El proyecto se organiza en módulos desacoplados que comparten un núcleo común. Cada
módulo puede usarse de forma independiente o combinarse mediante la CLI o la GUI.

## 2. Principios de diseño

- **Modularidad**: cada responsabilidad vive en su propio módulo.
- **Reutilización**: la CLI y la GUI consumen el mismo motor (`core`).
- **Portabilidad**: soporte previsto para Linux, Windows, macOS, FreeBSD, OpenBSD,
  Solaris, IRIX, HP-UX, NetBSD, Sun OS, Amiga y otros.
- **Rendimiento**: diseño orientado a escaneos rápidos de redes grandes, con
  paralelismo y control de concurrencia.
- **Seguridad y ética**: uso responsable, registro de acciones y resultados
  auditables.
- **Extensibilidad**: técnicas de escaneo y salidas pluggables.

## 3. Componentes del conjunto Net-Map

| Componente        | Responsabilidad                                                        |
|-------------------|------------------------------------------------------------------------|
| `netmap` (CLI)    | Escaneo y auditoría desde línea de comandos.                           |
| `netmap-gui`      | Interfaz gráfica avanzada y visor de resultados.                       |
| `netcat-map`      | Transferencia, redirección y depuración de datos.                      |
| `netdiff`         | Comparación de resultados de escaneo.                                  |
| `netping`         | Generación de paquetes y análisis de respuestas.                       |
| `netmap-inventory`| Inventario de red, cronogramas de actualización y uptime.              |

## 4. Capas de la arquitectura
┌─────────────────────────────────────────────┐
│ Interfaz de usuario │
│ ├─ CLI (src/cli) │
│ └─ GUI + visor (src/gui) │
├─────────────────────────────────────────────┤
│ Servicios de alto nivel │
│ ├─ Transferencia/redirección (src/transfer)│
│ ├─ Comparación de resultados (src/diff) │
│ └─ Inventario y uptime (src/inventory) │
├─────────────────────────────────────────────┤
│ Motor de descubrimiento y auditoría (core) │
│ ├─ Descubrimiento de hosts │
│ ├─ Escaneo de puertos TCP/UDP │
│ ├─ Detección de servicios y versiones │
│ ├─ Detección de SO │
│ └─ Detección de filtros/firewalls │
├─────────────────────────────────────────────┤
│ Capa de paquetes IP sin procesar │
│ └─ (src/packets) │
├─────────────────────────────────────────────┤
│ Sistema operativo y red │
└─────────────────────────────────────────────┘


## 5. Módulos y responsabilidades

### 5.1 `src/core` — Motor de descubrimiento y auditoría

Orquesta las técnicas de escaneo y consolida resultados. Expone una API interna
consumida por CLI, GUI y servicios. Responsabilidades:

- Coordinar barridos de ping y descubrimiento de hosts.
- Ejecutar escaneos de puertos TCP y UDP.
- Detectar servicios (nombre y versión de la aplicación).
- Detectar sistema operativo y versión.
- Identificar filtros de paquetes/firewalls y obstáculos de red.
- Aplicar concurrencia, timeouts y reintentos.

### 5.2 `src/packets` — Paquetes IP sin procesar

Genera, envía, captura y analiza paquetes IP sin procesar. Es la base de las
técnicas de escaneo y de `netping`. Responsabilidades:

- Construcción y parseo de cabeceras y payloads.
- Envío y recepción a bajo nivel.
- Análisis de respuestas para inferir estado de hosts, puertos y filtros.

### 5.3 `src/cli` — Línea de comandos

Interfaz principal para usuarios y automatización. Debe permitir un inicio simple
(por ejemplo, un escaneo con detección avanzada sobre un objetivo) y opciones
avanzadas para expertos. Ver `uso-cli.md`.

### 5.4 `src/gui` — Interfaz gráfica y visor

Interfaz gráfica avanzada y visor de resultados. Consume el mismo motor que la CLI.
Ver `uso-gui.md`.

### 5.5 `src/transfer` — Transferencia, redirección y depuración

Equivalente funcional a `netcat-map`: transferencia de datos, redirección y
depuración entre hosts.

### 5.6 `src/diff` — Comparación de resultados

Equivalente funcional a `netdiff`: compara dos resultados de escaneo y resalta
diferencias (hosts, puertos, servicios, versiones, SO).

### 5.7 `src/inventory` — Inventario, cronogramas y uptime

Inventario de red, gestión de cronogramas de actualización de servicios y
monitorización del tiempo de actividad de hosts o servicios. Ver
`inventario-y-uptime.md`.

## 6. Flujo de datos

1. El usuario define un objetivo y opciones (CLI o GUI).
2. `core` selecciona las técnicas y consulta a `packets` para emitir/recibir.
3. `packets` devuelve respuestas crudas.
4. `core` interpreta respuestas y produce resultados estructurados.
5. Los resultados se entregan a la interfaz, a `diff` y/o a `inventory`.
6. `inventory` persiste el estado para cronogramas y uptime.

## 7. Portabilidad

- Abstracción de la capa de red para adaptar el acceso a paquetes sin procesar por
  sistema operativo.
- Empaquetado oficial por plataforma en `packaging/linux`, `packaging/windows` y
  `packaging/macos`, extensible a otros sistemas.

## 8. Rendimiento y escalabilidad

- Concurrencia configurable y control de recursos.
- Diseño apto para cientos de miles de máquinas.
- Resultados estructurados para procesamiento posterior.

## 9. Seguridad y ética

- Uso previsto en redes propias o con autorización explícita.
- Registro de acciones y resultados auditables.
- Política de reporte de vulnerabilidades en `SECURITY.md`.

## 10. Fuera de alcance

- Modo monitor. No forma parte de Net-Map.

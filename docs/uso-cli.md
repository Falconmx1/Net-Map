# Uso de la CLI de Net-Map (`netmap`)

## 1. Introducción

`netmap` es el ejecutable clásico de línea de comandos de Net-Map. Comparte el mismo
motor que la GUI, por lo que los resultados son consistentes entre ambas interfaces.
Está pensado tanto para usuarios que inician con algo sencillo como para expertos que
necesitan opciones avanzadas.

> Uso responsable: escanea únicamente redes propias o para las que tengas
> autorización explícita.

## 2. Inicio rápido

Un escaneo con detección avanzada sobre un objetivo:
netmap -v -A targethost

Donde `targethost` puede ser un host individual, un rango o una red.

## 3. Sintaxis general
netmap [opciones] <objetivo>



- `<objetivo>`: host, rango o red a escanear.
- `[opciones]`: modificadores del escaneo y de la salida.

## 4. Opciones principales (referencia funcional)

> Esta sección describe la intención de cada opción. La lista definitiva se
> documentará junto con la implementación.

### 4.1 Descubrimiento de hosts
- Barridos de ping y variantes para determinar hosts disponibles.

### 4.2 Escaneo de puertos
- Escaneo TCP.
- Escaneo UDP.
- Selección de puertos o rangos.

### 4.3 Detección de servicios
- Identificación de nombre y versión de la aplicación por servicio.

### 4.4 Detección de sistema operativo
- Inferencia de SO y versión.

### 4.5 Detección de filtros/firewalls
- Identificación de tipos de filtros de paquetes y obstáculos de red.

### 4.6 Verbosidad y salida
- Niveles de detalle.
- Formatos de salida estructurados para inventario y comparación.

### 4.7 Rendimiento
- Concurrencia y timeouts configurables para redes grandes.

## 5. Ejemplos de uso (conceptuales)

- Escaneo de un host individual con detección avanzada.
- Descubrimiento de hosts en una red.
- Escaneo de puertos TCP y UDP en un rango.
- Detección de servicios y versiones.
- Detección de SO.
- Identificación de filtros/firewalls.
- Salida estructurada para alimentar `netdiff` o `netmap-inventory`.

## 6. Componentes relacionados

- `netcat-map`: transferencia, redirección y depuración de datos.
- `netdiff`: comparación de resultados de escaneo.
- `netping`: generación de paquetes y análisis de respuestas.
- `netmap-inventory`: inventario, cronogramas y uptime.

## 7. Buenas prácticas

- Documentar el objetivo y la autorización del escaneo.
- Ajustar concurrencia y timeouts según el tamaño de la red.
- Guardar resultados estructurados para auditoría y comparación.

## 8. Fuera de alcance

- Modo monitor. No forma parte de Net-Map.

# Inventario, cronogramas de actualización y uptime en Net-Map

## 1. Introducción

Además del descubrimiento y la auditoría, Net-Map ayuda a administradores de sistemas
y redes con tareas operativas: inventario de red, gestión de cronogramas de
actualización de servicios y monitorización del tiempo de actividad de hosts o
servicios.

Este documento describe el propósito de estas capacidades y cómo se integran con el
resto de Net-Map.

## 2. Inventario de red

### 2.1 Propósito
Mantener un registro estructurado de hosts, servicios, versiones y sistemas
operativos detectados.

### 2.2 Fuente de datos
Resultados de escaneo generados por `core` a través de la CLI o la GUI.

### 2.3 Uso
- Consulta de hosts y servicios.
- Base para cronogramas de actualización.
- Base para monitorización de uptime.

## 3. Cronogramas de actualización de servicios

### 3.1 Propósito
Gestionar cuándo deben actualizarse los servicios detectados.

### 3.2 Insumos
- Inventario de servicios y versiones.
- Resultados de escaneos sucesivos.

### 3.3 Uso
- Planificación de actualizaciones.
- Seguimiento de cambios entre escaneos (con `netdiff`).

## 4. Monitorización del tiempo de actividad (uptime)

### 4.1 Propósito
Supervisar la disponibilidad de hosts o servicios a lo largo del tiempo.

### 4.2 Insumos
- Resultados de escaneos periódicos.
- Inventario de hosts y servicios.

### 4.3 Uso
- Detección de caídas y recuperaciones.
- Historial de disponibilidad.

## 5. Integración con otros componentes

- `netmap` (CLI) y `netmap-gui`: generan resultados de escaneo.
- `netdiff`: compara resultados para detectar cambios.
- `netcat-map`: transferencia, redirección y depuración de datos.
- `netping`: generación de paquetes y análisis de respuestas.

## 6. Buenas prácticas

- Documentar el objetivo y la autorización de los escaneos.
- Guardar resultados estructurados para trazabilidad.
- Programar escaneos periódicos para inventario y uptime.

## 7. Fuera de alcance

- Modo monitor. No forma parte de Net-Map.

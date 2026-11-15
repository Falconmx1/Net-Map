# Técnicas de escaneo de Net-Map

## 1. Introducción

Net-Map utiliza paquetes IP sin procesar de formas innovadoras para determinar
características de la red. Este documento describe las técnicas previstas, su
propósito y las consideraciones de uso.

> Uso responsable: aplica estas técnicas únicamente en redes propias o con
> autorización explícita.

## 2. Descubrimiento de hosts

Determina qué hosts están disponibles en la red mediante barridos de ping y
variantes. Permite identificar hosts activos antes de profundizar en puertos y
servicios.

## 3. Escaneo de puertos

### 3.1 TCP
Identifica puertos TCP abiertos, cerrados o filtrados mediante el envío y análisis de
paquetes.

### 3.2 UDP
Identifica servicios UDP y su estado, con manejo de timeouts y reintentos.

## 4. Detección de servicios y versiones

Determina el nombre y la versión de la aplicación que ofrece cada servicio, a partir
del análisis de respuestas.

## 5. Detección de sistema operativo

Infiere el sistema operativo y su versión a partir del comportamiento de la pila de
red y las respuestas observadas.

## 6. Detección de filtros de paquetes y firewalls

Identifica el tipo de filtros de paquetes/firewalls en uso y otros obstáculos de red,
analizando patrones de respuesta y descarte.

## 7. Técnicas para atravesar obstáculos

Net-Map está diseñada para mapear redes con filtros IP, cortafuegos, enrutadores y
otros obstáculos, combinando técnicas y ajustando parámetros de escaneo.

## 8. Rendimiento

- Concurrencia configurable.
- Timeouts y reintentos ajustables.
- Diseño apto para redes grandes y hosts individuales.

## 9. Resultados

Los resultados se estructuran para alimentar la CLI, la GUI, `netdiff` y
`netmap-inventory`.

## 10. Fuera de alcance

- Modo monitor. No forma parte de Net-Map.

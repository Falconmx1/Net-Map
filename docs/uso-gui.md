# Uso de la GUI de Net-Map (`netmap-gui`)

## 1. Introducción

`netmap-gui` es la interfaz gráfica avanzada y el visor de resultados de Net-Map.
Consume el mismo motor que la CLI, por lo que los resultados son consistentes entre
ambas interfaces.

> Uso responsable: escanea únicamente redes propias o para las que tengas
> autorización explícita.

## 2. Objetivo de la GUI

- Facilitar escaneos sin memorizar opciones de línea de comandos.
- Visualizar resultados de forma clara y navegable.
- Servir como visor de resultados generados por la CLI u otros componentes.
- Apoyar tareas de inventario, cronogramas de actualización y uptime.

## 3. Flujo de trabajo típico

1. Definir el objetivo (host, rango o red).
2. Seleccionar el tipo de escaneo y las opciones deseadas.
3. Ejecutar el escaneo.
4. Revisar resultados en el visor.
5. Exportar o comparar resultados según sea necesario.

## 4. Áreas funcionales de la interfaz

> Esta sección describe la intención de cada área. El diseño definitivo se
> documentará junto con la implementación.

### 4.1 Configuración del objetivo
- Entrada de host, rango o red.
- Validación de la entrada.

### 4.2 Selección de opciones
- Descubrimiento de hosts.
- Escaneo de puertos TCP/UDP.
- Detección de servicios y versiones.
- Detección de SO.
- Detección de filtros/firewalls.
- Concurrencia y timeouts.

### 4.3 Ejecución y progreso
- Inicio, pausa y cancelación del escaneo.
- Indicadores de progreso.

### 4.4 Visor de resultados
- Lista de hosts y estado.
- Puertos y servicios detectados.
- Sistema operativo inferido.
- Filtros/firewalls identificados.
- Búsqueda y filtrado de resultados.

### 4.5 Exportación y comparación
- Exportación de resultados estructurados.
- Integración con `netdiff` para comparar escaneos.
- Integración con `netmap-inventory` para inventario y uptime.

## 5. Componentes relacionados

- `netmap` (CLI): misma funcionalidad desde línea de comandos.
- `netdiff`: comparación de resultados.
- `netmap-inventory`: inventario, cronogramas y uptime.

## 6. Buenas prácticas

- Documentar el objetivo y la autorización del escaneo.
- Ajustar concurrencia y timeouts según el tamaño de la red.
- Guardar resultados para auditoría y comparación.

## 7. Fuera de alcance

- Modo monitor. No forma parte de Net-Map.

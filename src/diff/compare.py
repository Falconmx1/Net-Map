"""Comparación de resultados de escaneo."""

from __future__ import annotations

from typing import Any


def diff_results(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    """Compara dos resultados de escaneo y devuelve diferencias.

    Args:
        previous: Resultado anterior.
        current: Resultado actual.

    Returns:
        Diccionario con hosts/puertos agregados, eliminados y cambiados.
    """
    prev_hosts = set(previous.get("hosts", {}).keys()) if isinstance(previous.get("hosts"), dict) else set()
    curr_hosts = set(current.get("hosts", {}).keys()) if isinstance(current.get("hosts"), dict) else set()

    added_hosts = sorted(curr_hosts - prev_hosts)
    removed_hosts = sorted(prev_hosts - curr_hosts)

    changed_ports: dict[str, dict[str, Any]] = {}
    prev_ports = previous.get("ports", {})
    curr_ports = current.get("ports", {})
    if isinstance(prev_ports, dict) and isinstance(curr_ports, dict):
        for host in sorted(set(prev_ports) & set(curr_ports)):
            if prev_ports[host] != curr_ports[host]:
                changed_ports[host] = {
                    "previous": prev_ports[host],
                    "current": curr_ports[host],
                }

    return {
        "added_hosts": added_hosts,
        "removed_hosts": removed_hosts,
        "changed_ports": changed_ports,
    }

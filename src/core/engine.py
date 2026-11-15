"""Motor de descubrimiento y auditoría de Net-Map."""

from __future__ import annotations

from typing import Iterable

from src.packets.packet import (
    build_icmp_echo,
    build_tcp_syn,
    send_and_receive,
)

COMMON_PORTS: tuple[int, ...] = (22, 80, 443, 445, 3389, 8080)


class DiscoveryEngine:
    """Motor central consumido por CLI y GUI."""

    def __init__(self, target: str, timeout: float = 1.0) -> None:
        self.target: str = target
        self.timeout: float = timeout

    def is_host_up(self) -> bool:
        """Determina si el host responde a ICMP echo."""
        response = send_and_receive(build_icmp_echo(self.target), timeout=self.timeout)
        return response is not None

    def scan_ports(self, ports: Iterable[int] | None = None) -> dict[int, str]:
        """Escanea puertos TCP y devuelve estado por puerto.

        Returns:
            Diccionario puerto -> "open" | "closed_or_filtered".
        """
        if ports is None:
            ports = COMMON_PORTS
        results: dict[int, str] = {}
        for port in ports:
            response = send_and_receive(
                build_tcp_syn(self.target, int(port)), timeout=self.timeout
            )
            if response is None:
                results[int(port)] = "closed_or_filtered"
            elif response.haslayer("TCP") and "S" in str(response["TCP"].flags):
                results[int(port)] = "open"
            else:
                results[int(port)] = "closed_or_filtered"
        return results

    def scan(self) -> dict[str, object]:
        """Ejecuta descubrimiento y escaneo básico del objetivo."""
        return {
            "target": self.target,
            "host_up": self.is_host_up(),
            "ports": self.scan_ports(),
        }

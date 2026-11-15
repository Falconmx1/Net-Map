"""Construcción y análisis de paquetes IP sin procesar con scapy."""

from __future__ import annotations

from typing import Any

from scapy.all import IP, TCP, UDP, ICMP, sr1  # type: ignore


def build_tcp_syn(dst: str, dport: int, sport: int = 40000) -> Any:
    """Construye un paquete TCP SYN hacia dst:dport."""
    return IP(dst=dst) / TCP(sport=sport, dport=dport, flags="S")


def build_udp(dst: str, dport: int, sport: int = 40000) -> Any:
    """Construye un paquete UDP hacia dst:dport."""
    return IP(dst=dst) / UDP(sport=sport, dport=dport)


def build_icmp_echo(dst: str) -> Any:
    """Construye un ICMP echo request hacia dst."""
    return IP(dst=dst) / ICMP()


def send_and_receive(packet: Any, timeout: float = 1.0) -> Any:
    """Envía un paquete y devuelve la primera respuesta o None."""
    return sr1(packet, timeout=timeout, verbose=0)


def analyze_response(response: Any) -> dict[str, object]:
    """Extrae campos relevantes de una respuesta scapy."""
    if response is None:
        return {"responded": False}
    result: dict[str, object] = {"responded": True}
    if response.haslayer(IP):
        result["src"] = response[IP].src
        result["ttl"] = response[IP].ttl
    if response.haslayer(TCP):
        result["tcp_flags"] = str(response[TCP].flags)
        result["tcp_dport"] = response[TCP].dport
    if response.haslayer(UDP):
        result["udp_sport"] = response[UDP].sport
    if response.haslayer(ICMP):
        result["icmp_type"] = response[ICMP].type
    return result

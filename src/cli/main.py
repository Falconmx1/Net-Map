"""Punto de entrada de la CLI de Net-Map (`netmap`)."""

from __future__ import annotations

import argparse
import json
import sys
from typing import Sequence

from src.core.engine import DiscoveryEngine


def build_parser() -> argparse.ArgumentParser:
    """Construye el parser de argumentos de la CLI."""
    parser = argparse.ArgumentParser(
        prog="netmap",
        description="Net-Map: descubrimiento de redes y auditoría de seguridad.",
    )
    parser.add_argument("target", help="Host, rango o red a escanear.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Salida detallada.")
    parser.add_argument(
        "-A",
        "--aggressive",
        action="store_true",
        help="Escaneo avanzado (hosts + puertos comunes).",
    )
    parser.add_argument(
        "-p",
        "--ports",
        default="",
        help="Lista de puertos separados por coma (ej. 22,80,443).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Salida en JSON.",
    )
    return parser


def parse_ports(value: str) -> list[int]:
    """Convierte '22,80,443' en [22, 80, 443]."""
    if not value:
        return []
    ports: list[int] = []
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        ports.append(int(item))
    return ports


def main(argv: Sequence[str] | None = None) -> int:
    """Punto de entrada principal de la CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    engine = DiscoveryEngine(args.target)

    if args.aggressive:
        result: dict[str, object] = engine.scan()
    else:
        ports = parse_ports(args.ports) or None
        result = {
            "target": args.target,
            "host_up": engine.is_host_up(),
            "ports": engine.scan_ports(ports),
        }

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        if args.verbose:
            print(f"Objetivo: {result['target']}")
        print(f"Host activo: {result['host_up']}")
        ports = result.get("ports", {})
        if isinstance(ports, dict):
            for port, state in ports.items():
                print(f"  Puerto {port}: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

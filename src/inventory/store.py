"""Inventario, cronogramas y uptime."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


class Inventory:
    """Inventario de red con persistencia JSON."""

    def __init__(self, path: str | Path = "inventory.json") -> None:
        self.path = Path(path)
        self.hosts: dict[str, dict[str, Any]] = {}
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            try:
                data = json.loads(self.path.read_text(encoding="utf-8"))
                if isinstance(data, dict):
                    self.hosts = data
            except (json.JSONDecodeError, OSError):
                self.hosts = {}

    def save(self) -> None:
        """Persiste el inventario en disco."""
        self.path.write_text(
            json.dumps(self.hosts, indent=2, default=str),
            encoding="utf-8",
        )

    def add_host(self, host: str, data: dict[str, Any] | None = None) -> None:
        """Agrega o actualiza un host."""
        self.hosts[host] = dict(data or {})
        self.save()

    def list_hosts(self) -> list[str]:
        """Lista los hosts registrados."""
        return sorted(self.hosts.keys())

    def record_uptime(self, host: str, up: bool) -> None:
        """Registra una comprobación de uptime para un host."""
        entry = self.hosts.setdefault(host, {})
        checks = entry.setdefault("uptime", [])
        if isinstance(checks, list):
            checks.append({"timestamp": time.time(), "up": up})
        self.save()

    def uptime(self, host: str) -> float | None:
        """Devuelve el porcentaje de uptime registrado para un host."""
        entry = self.hosts.get(host, {})
        checks = entry.get("uptime", [])
        if not isinstance(checks, list) or not checks:
            return None
        up_count = sum(1 for c in checks if isinstance(c, dict) and c.get("up"))
        return up_count / len(checks)

"""Pruebas del módulo inventory."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from src.inventory.store import Inventory


class TestInventory(unittest.TestCase):
    """Pruebas de inventario y uptime."""

    def test_add_and_list(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            inv = Inventory(Path(tmp) / "inv.json")
            inv.add_host("10.0.0.1", {"os": "Linux"})
            self.assertEqual(inv.list_hosts(), ["10.0.0.1"])

    def test_uptime(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            inv = Inventory(Path(tmp) / "inv.json")
            inv.record_uptime("h", True)
            inv.record_uptime("h", False)
            self.assertEqual(inv.uptime("h"), 0.5)


if __name__ == "__main__":
    unittest.main()

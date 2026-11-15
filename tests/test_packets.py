"""Pruebas del módulo de paquetes."""

from __future__ import annotations

import unittest

from src.packets.packet import analyze_response


class TestPackets(unittest.TestCase):
    """Pruebas básicas de análisis de respuestas."""

    def test_none_response(self) -> None:
        self.assertEqual(analyze_response(None), {"responded": False})


if __name__ == "__main__":
    unittest.main()

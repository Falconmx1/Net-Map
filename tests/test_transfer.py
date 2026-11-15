"""Pruebas del módulo transfer."""

from __future__ import annotations

import unittest

from src.transfer.transfer import transfer


class TestTransfer(unittest.TestCase):
    """Pruebas básicas de transferencia."""

    def test_transfer_fails_cleanly(self) -> None:
        # Puerto cerrado en localhost debe devolver 1 sin lanzar excepción.
        self.assertEqual(transfer("x", "127.0.0.1", port=1, timeout=0.2), 1)


if __name__ == "__main__":
    unittest.main()

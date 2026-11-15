"""Pruebas de la CLI."""

from __future__ import annotations

import unittest

from src.cli.main import parse_ports


class TestCli(unittest.TestCase):
    """Pruebas de parseo de puertos."""

    def test_parse_ports_empty(self) -> None:
        self.assertEqual(parse_ports(""), [])

    def test_parse_ports_list(self) -> None:
        self.assertEqual(parse_ports("22,80,443"), [22, 80, 443])


if __name__ == "__main__":
    unittest.main()

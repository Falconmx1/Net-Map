"""Pruebas del módulo diff."""

from __future__ import annotations

import unittest

from src.diff.compare import diff_results


class TestDiff(unittest.TestCase):
    """Pruebas de comparación de resultados."""

    def test_added_and_removed(self) -> None:
        prev = {"hosts": {"a": {}, "b": {}}}
        curr = {"hosts": {"b": {}, "c": {}}}
        result = diff_results(prev, curr)
        self.assertEqual(result["added_hosts"], ["c"])
        self.assertEqual(result["removed_hosts"], ["a"])

    def test_changed_ports(self) -> None:
        prev = {"ports": {"h": {22: "open"}}}
        curr = {"ports": {"h": {22: "closed_or_filtered"}}}
        result = diff_results(prev, curr)
        self.assertIn("h", result["changed_ports"])


if __name__ == "__main__":
    unittest.main()

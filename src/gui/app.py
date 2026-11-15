"""GUI de Net-Map con tkinter (incluido en Python)."""

from __future__ import annotations

import json
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext

from src.core.engine import DiscoveryEngine


class NetMapGUI:
    """Interfaz gráfica y visor de resultados de Net-Map."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Net-Map")
        self.root.geometry("700x500")
        self._build_widgets()

    def _build_widgets(self) -> None:
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=8, pady=8)

        tk.Label(frame, text="Objetivo:").pack(side=tk.LEFT)
        self.target_entry = tk.Entry(frame, width=30)
        self.target_entry.pack(side=tk.LEFT, padx=4)

        self.scan_button = tk.Button(frame, text="Escanear", command=self._on_scan)
        self.scan_button.pack(side=tk.LEFT, padx=4)

        self.output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.output.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    def _on_scan(self) -> None:
        target = self.target_entry.get().strip()
        if not target:
            messagebox.showwarning("Net-Map", "Ingresa un objetivo.")
            return
        self.scan_button.config(state=tk.DISABLED)
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, f"Escaneando {target}...\n")
        threading.Thread(target=self._run_scan, args=(target,), daemon=True).start()

    def _run_scan(self, target: str) -> None:
        try:
            engine = DiscoveryEngine(target)
            result = engine.scan()
            text = json.dumps(result, indent=2, default=str)
        except Exception as exc:  # noqa: BLE001
            text = f"Error: {exc}"
        self.root.after(0, self._show_result, text)

    def _show_result(self, text: str) -> None:
        self.output.insert(tk.END, text + "\n")
        self.scan_button.config(state=tk.NORMAL)


def run() -> int:
    """Inicia la GUI de Net-Map."""
    root = tk.Tk()
    NetMapGUI(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

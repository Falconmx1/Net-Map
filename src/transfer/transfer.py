"""Transferencia, redirección y depuración de datos (netcat-map)."""

from __future__ import annotations

import socket


def transfer(source: str, destination: str, port: int = 9000, timeout: float = 5.0) -> int:
    """Transfiere un mensaje de source a destination vía TCP.

    Args:
        source: Texto a enviar.
        destination: Host destino.
        port: Puerto TCP destino.
        timeout: Timeout en segundos.

    Returns:
        Código de salida (0 = éxito, 1 = error).
    """
    try:
        with socket.create_connection((destination, port), timeout=timeout) as sock:
            sock.sendall(source.encode("utf-8"))
        return 0
    except OSError:
        return 1

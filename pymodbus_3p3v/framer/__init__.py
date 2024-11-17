"""Framer."""
__all__ = [
    "FramerBase",
    "FramerType",
    "FramerAscii",
    "FramerRTU",
    "FramerSocket",
    "FramerTLS"
]

from pymodbus_3p3v.framer.ascii import FramerAscii
from pymodbus_3p3v.framer.base import FramerBase, FramerType
from pymodbus_3p3v.framer.rtu import FramerRTU
from pymodbus_3p3v.framer.socket import FramerSocket
from pymodbus_3p3v.framer.tls import FramerTLS


FRAMER_NAME_TO_CLASS = {
    FramerType.ASCII: FramerAscii,
    FramerType.RTU: FramerRTU,
    FramerType.SOCKET: FramerSocket,
    FramerType.TLS: FramerTLS,
}

"""Pymodbus: Modbus Protocol Implementation.

Released under the BSD license
"""

__all__ = [
    "ExceptionResponse",
    "FramerType",
    "ModbusException",
    "pymodbus_apply_logging_config",
    "__version__",
    "__version_full__",
]

from pymodbus_3p3v.exceptions import ModbusException
from pymodbus_3p3v.framer import FramerType
from pymodbus_3p3v.logging import pymodbus_apply_logging_config
from pymodbus_3p3v.pdu import ExceptionResponse


__version__ = "3.7.4.5"
__version_full__ = f"[pymodbus, version {__version__}]"

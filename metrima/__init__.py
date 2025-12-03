from .main import _make_divider, add, subtract, mul, div
from .fx import Fx, fx
from .custerror import UnexpectedTypeError
from .tests import test_main

__all__ = [
    "add",
    "subtract",
    "mul",
    "div",

    "Fx",
    "fx",

    "UnexpectedTypeError",
]

__version__ = "0.1.0"
from __future__ import annotations
from metrima.core.fixed import Fx

# --- In-place operators ---#
def __iadd__(self: Fx, other: Fx | int | float) -> Fx:
    result = self + other
    self.value = result.value
    self.scale = result.scale
    return self


def __isub__(self: Fx, other: Fx | int | float) -> Fx:
    result = self - other
    self.value = result.value
    self.scale = result.scale
    return self


def __imul__(self: Fx, other: Fx | int | float) -> Fx:
    result = self * other
    self.value = result.value
    self.scale = result.scale
    return self


def __itruediv__(self: Fx, other: Fx | int | float) -> Fx:
    result = self / other
    self.value = result.value
    self.scale = result.scale
    return self


def __ifloordiv__(self: Fx, other: Fx | int | float) -> Fx:
    result = self // other
    self.value = result.value
    self.scale = result.scale
    return self


def __ipow__(self: Fx, other: Fx | int | float) -> Fx:
    result = self ** other
    self.value = result.value
    self.scale = result.scale
    return self


def __imod__(self: Fx, other: Fx | int | float) -> Fx:
    result = self % other
    self.value = result.value
    self.scale = result.scale
    return self
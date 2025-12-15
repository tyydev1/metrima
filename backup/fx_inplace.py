# --- In-place operators ---#
def __iadd__(self, other: Fx | int | float) -> Fx:
    result = self + other
    self.value = result.value
    self.scale = result.scale
    return self


def __isub__(self, other: Fx | int | float) -> Fx:
    result = self - other
    self.value = result.value
    self.scale = result.scale
    return self


def __imul__(self, other: Fx | int | float) -> Fx:
    result = self * other
    self.value = result.value
    self.scale = result.scale
    return self


def __itruediv__(self, other: Fx | int | float) -> Fx:
    result = self / other
    self.value = result.value
    self.scale = result.scale
    return self


def __ifloordiv__(self, other: Fx | int | float) -> Fx:
    result = self // other
    self.value = result.value
    self.scale = result.scale
    return self


def __ipow__(self, other: Fx | int | float) -> Fx:
    result = self ** other
    self.value = result.value
    self.scale = result.scale
    return self


def __imod__(self, other: Fx | int | float) -> Fx:
    result = self % other
    self.value = result.value
    self.scale = result.scale
    return self
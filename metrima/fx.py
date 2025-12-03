from typing import Any
from tinycolors import cprint, clib
from custerror import UnexpectedTypeError



class Fx:
    def __init__(self, value: str | float | int) -> None:
        s = str(value)
        if '.' in s:
            whole, frac = s.split('.')
            self.scale: int = len(frac)
            self.value: int = int(whole + frac)
        else:
            self.scale: int = 0
            self.value: int = int(s)

        self._normalize()

    def _normalize(self):
        """Remove trailing zeros from the fractional part"""
        if self.value == 0:
            self.scale = 0
            return

        while self.scale > 0 and self.value % 10 == 0:
            self.value //= 10
            self.scale -= 1

    def _align(self, other: Fx) -> tuple[int, int, int]:
        if not isinstance(other, Fx):
            raise UnexpectedTypeError(f"Unexpected type {type(other)}")

        if self.scale == other.scale:
            return self.value, other.value, self.scale
        if self.scale > other.scale:
            diff = self.scale - other.scale
            return self.value, other.value * (10 ** diff), self.scale
        diff = other.scale - self.scale
        return self.value * (10 ** diff), other.value, other.scale

    def __repr__(self):
        return f"Fx(value={self.value}, scale={self.scale})"

    #--- Conversions ---#
    def __float__(self):
        return self.value / (10 ** self.scale)

    def __int__(self):
        return int(float(self))

    def __str__(self):
        if self.scale == 0:
            return str(self.value)

        if self.value == 0:
            return "0"

        s = str(self.value).zfill(self.scale + 1)
        return s[:-self.scale] + '.' + s[-self.scale:]

    #--- Miscellaneous ---#
    def __neg__(self) -> Fx:
        result = Fx.__new__(Fx)
        result.value = -self.value
        result.scale = self.scale
        result._normalize()
        return result

    def __pos__(self) -> Fx:
        result = Fx.__new__(Fx)
        result.value = self.value
        result.scale = self.scale
        result._normalize()
        return result

    def __abs__(self) -> Fx:
        result = Fx.__new__(Fx)
        result.value = abs(self.value)
        result.scale = self.scale
        result._normalize()
        return result

    def __round__(self, n: int = 0) -> Fx:
        return Fx(round(float(self), n))

    def __index__(self) -> int:
        return int(self)

    def __format__(self, format_spec: str) -> str:
        return format(float(self), format_spec)

    #--- Comparisons ---#
    def __eq__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a == b
        if isinstance(other, (int, float)):
            return float(self) == other
        return False
    def __ne__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a != b
        if isinstance(other, (int, float)):
            return float(self) != other
        return False

    def __gt__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a > b
        if isinstance(other, (int, float)):
            return float(self) > other
        return False
    def __ge__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a >= b
        if isinstance(other, (int, float)):
            return float(self) >= other
        return False

    def __lt__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a < b
        if isinstance(other, (int, float)):
            return float(self) < other
        return False
    def __le__(self, other):
        if isinstance(other, Fx):
            a, b, _ = self._align(other)
            return a <= b
        if isinstance(other, (int, float)):
            return float(self) <= other
        return False

    def __bool__(self):
        return self.value != 0

    #--- Arithmetics --#
    def __add__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        a, b, scale = self._align(other)
        result_value = a + b
        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
        result._normalize()
        return result

    def __sub__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        a, b, scale = self._align(other)
        result_value = a - b
        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
        result._normalize()
        return result

    def __mul__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        result_value = self.value * other.value
        scale = self.scale + other.scale
        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
        result._normalize()
        return result

    def __truediv__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        if float(other) == 0:
            raise ZeroDivisionError
        return Fx(float(self) / float(other))

    def __floordiv__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        if float(other) == 0:
            raise ZeroDivisionError
        return Fx(float(self) // float(other))

    def __pow__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        base = float(self)
        exponent = float(other)
        result = base ** exponent
        return Fx(result)

    def __mod__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)

        a, b, scale = self._align(other)

        result_value = a % b

        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
        result._normalize()
        return result

    #--- Right hand ---#
    def __radd__(self, other: int | float) -> Fx:
        return self + other

    def __rsub__(self, other: int | float) -> Fx:
        return Fx(other) - self

    def __rmul__(self, other: int | float) -> Fx:
        return self * other

    def __rtruediv__(self, other: int | float) -> Fx:
        return Fx(other) / self

    def __rfloordiv__(self, other: int | float) -> Fx:
        return Fx(other) // self

    def __rmod__(self, other: int | float) -> Fx:
        return Fx(other) % self

    def __rpow__(self, other: int | float) -> Fx:
        return Fx(other) ** self

    #--- In-place operators ---#
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


def fx(value: str | int | float) -> Fx:
    """
    Converts the following `value` to fx, if possible.
    :param value:
    :return:
    """
    return Fx(value)

if __name__ == "__main__":
    from tests import test_fx
    test_fx()
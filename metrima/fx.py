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
        return f"Fx(value={self.value})"

    #--- Conversions ---#
    def __float__(self):
        return self.value / (10 ** self.scale)

    def __int__(self):
        return int(float(self))

    def __str__(self):
        if self.scale == 0:
            return str(self.value)
        s = str(self.value).zfill(self.scale + 1)
        return s[:-self.scale] + '.' + s[-self.scale:]

    #--- Miscellaneous ---#
    def __neg__(self) -> Fx:
        return Fx(f"{-float(self)}")

    def __pos__(self) -> Fx:
        return Fx(f"{+float(self)}")

    def __abs__(self) -> Fx:
        return Fx(f"{abs(float(self))}")

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
        return result

    def __sub__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        a, b, scale = self._align(other)
        result_value = a - b
        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
        return result

    def __mul__(self, other: Fx | float | int) -> Fx:
        if isinstance(other, (int, float)):
            other = fx(other)
        result_value = self.value * other.value
        scale = self.scale + other.scale
        result = Fx.__new__(Fx)
        result.value = result_value
        result.scale = scale
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
        return Fx(float(self) % float(other))

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
        result = self + other  # use __add__ for calculation
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
    return Fx(value)

if __name__ == "__main__":
    test_count = 0
    pass_count = 0

    cprint("Fx class testing", as_="bold white on black")
    print()


    pass_local = 0
    total_local = 6

    cprint("repr(Fx()) and str(Fx())", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1, expected2, expected3 = 'Fx(value=0)', 'Fx(value=0)', 'Fx(value=0)'
    actual1, actual2, actual3 = repr(Fx("0")), repr(Fx(0)), repr(Fx(0.0))

    cprint(f"repr(Fx(\"0\")) = {actual1}", "cyan")
    cprint(f"repr(Fx(0)) = {actual2}", "cyan")
    cprint(f"repr(Fx(0.0)) = {actual3}", "cyan")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    expected4, expected5, expected6 = "3.14", "42", "0.5"
    actual4, actual5, actual6 = str(Fx("3.14")), str(Fx(42)), str(Fx(0.5))

    cprint(f"str(Fx(\"3.14\")) = {actual4}", "cyan")
    cprint(f"str(Fx(42)) = {actual5}", "cyan")
    cprint(f"str(Fx(0.5)) = {actual6}", "cyan")
    cprint('-'*40, as_="bold white")

    if actual4 == expected4:
        pass_local += 1
    if actual5 == expected5:
        pass_local += 1
    if actual6 == expected6:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Addition: 1.432 + 5.1234", as_="bold yellow")
    cprint('-' * 40, as_="bold white")

    expected1 = str(Fx("6.5554"))
    actual1 = str(Fx("1.432") + Fx("5.1234"))
    cprint(f'Fx("1.432") + Fx("5.1234") = {actual1}', "cyan")

    expected2 = str(Fx("5.5"))
    actual2 = str(Fx(2) + Fx(3.5))
    cprint(f'Fx(2) + Fx(3.5) = {actual2}', "cyan")

    expected3 = str(Fx("0.019"))
    actual3 = str(Fx(0.01) + Fx(0.009))
    cprint(f'Fx(0.01) + Fx(0.009) = {actual3}', "cyan")

    cprint('-' * 40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Subtraction: 5.5 - 2.2", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("3.3"))
    actual1 = str(Fx("5.5") - Fx("2.2"))
    cprint(f'Fx("5.5") - Fx("2.2") = {actual1}', "cyan")

    expected2 = str(Fx("7"))
    actual2 = str(Fx(10) - 3)
    cprint(f'Fx(10) - 3 = {actual2}', "cyan")

    expected3 = str(Fx("4.5"))
    actual3 = str(7 - Fx(2.5))
    cprint(f'7 - Fx(2.5) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Multiplication: 1.5 * 2", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("3.0"))
    actual1 = str(Fx("1.5") * Fx("2"))
    cprint(f'Fx("1.5") * Fx("2") = {actual1}', "cyan")

    expected2 = str(Fx("7.5"))
    actual2 = str(Fx(3) * 2.5)
    cprint(f'Fx(3) * 2.5 = {actual2}', "cyan")

    expected3 = str(Fx("8.4"))
    actual3 = str(2 * Fx(4.2))
    cprint(f'2 * Fx(4.2) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Division: 3.6 / 1.2", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("3.0"))
    actual1 = str(Fx("3.6") / Fx("1.2"))
    cprint(f'Fx("3.6") / Fx("1.2") = {actual1}', "cyan")

    expected2 = str(Fx("2.5"))
    actual2 = str(Fx(5) / 2)
    cprint(f'Fx(5) / 2 = {actual2}', "cyan")

    expected3 = str(Fx("3.0"))
    actual3 = str(12 / Fx(4))
    cprint(f'12 / Fx(4) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Floor Division: 2.5 // 1.2", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("2.0"))
    actual1 = str(Fx("2.5") // Fx("1.2"))
    cprint(f'Fx("2.5") // Fx("1.2") = {actual1}', "cyan")

    expected2 = str(Fx("2.0"))
    actual2 = str(Fx(7) // 3)
    cprint(f'Fx(7) // 3 = {actual2}', "cyan")

    expected3 = str(Fx("2.0"))
    actual3 = str(10 // Fx(4))
    cprint(f'10 // Fx(4) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 4

    cprint("Comparisons", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = True
    actual1 = Fx("2.0") == Fx("2")
    cprint(f'Fx("2.0") == Fx("2") = {actual1}', "cyan")

    expected2 = False
    actual2 = Fx(3) != 3
    cprint(f'Fx(3) != 3 = {actual2}', "cyan")

    expected3 = True
    actual3 = Fx("1.5") > Fx("1.4")
    cprint(f'Fx("1.5") > Fx("1.4") = {actual3}', "cyan")

    expected4 = True
    actual4 = Fx("1.2") < 2
    cprint(f'Fx("1.2") < 2 = {actual4}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1
    if actual4 == expected4:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Modulo: 5.5 % 2", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("1.5"))
    actual1 = str(Fx("5.5") % Fx("2"))
    cprint(f'Fx("5.5") % Fx("2") = {actual1}', "cyan")

    expected2 = str(Fx("1.0"))
    actual2 = str(Fx(7) % 3)
    cprint(f'Fx(7) % 3 = {actual2}', "cyan")

    expected3 = str(Fx("0.0"))
    actual3 = str(10 % Fx(2.5))
    cprint(f'10 % Fx(2.5) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 3

    cprint("Power: 2 ** 3", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("8.0"))
    actual1 = str(Fx("2") ** Fx("3"))
    cprint(f'Fx("2") ** Fx("3") = {actual1}', "cyan")

    expected2 = str(Fx("9.0"))
    actual2 = str(Fx(3) ** 2)
    cprint(f'Fx(3) ** 2 = {actual2}', "cyan")

    expected3 = str(Fx("32.0"))
    actual3 = str(2 ** Fx(5))
    cprint(f'2 ** Fx(5) = {actual3}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 5

    cprint("Type Conversions", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = 3.14
    actual1 = float(Fx("3.14"))
    cprint(f'float(Fx("3.14")) = {actual1}', "cyan")

    expected2 = 42
    actual2 = int(Fx("42.7"))
    cprint(f'int(Fx("42.7")) = {actual2}', "cyan")

    expected3 = "5.5"
    actual3 = str(Fx(5.5))
    cprint(f'str(Fx(5.5)) = {actual3}', "cyan")

    expected4 = True
    actual4 = bool(Fx("3.14"))
    cprint(f'bool(Fx("3.14")) = {actual4}', "cyan")

    expected5 = False
    actual5 = bool(Fx(0))
    cprint(f'bool(Fx(0)) = {actual5}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1
    if actual4 == expected4:
        pass_local += 1
    if actual5 == expected5:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 4

    cprint("Unary Operations", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1 = str(Fx("-3.14"))
    actual1 = str(-Fx("3.14"))
    cprint(f'-Fx("3.14") = {actual1}', "cyan")

    expected2 = str(Fx("5.5"))
    actual2 = str(+Fx("5.5"))
    cprint(f'+Fx("5.5") = {actual2}', "cyan")

    expected3 = str(Fx("3.14"))
    actual3 = str(abs(Fx("-3.14")))
    cprint(f'abs(Fx("-3.14")) = {actual3}', "cyan")

    expected4 = str(Fx("3.1"))
    actual4 = str(round(Fx("3.14159"), 1))
    cprint(f'round(Fx("3.14159"), 1) = {actual4}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1
    if actual4 == expected4:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    pass_local = 0
    total_local = 4

    cprint("In-place Operations", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    x1 = Fx("5")
    x1 += Fx("3")
    expected1 = str(Fx("8"))
    actual1 = str(x1)
    cprint(f'x = Fx("5"); x += Fx("3"); x = {actual1}', "cyan")

    x2 = Fx("10")
    x2 -= 3
    expected2 = str(Fx("7"))
    actual2 = str(x2)
    cprint(f'x = Fx("10"); x -= 3; x = {actual2}', "cyan")

    x3 = Fx("4")
    x3 *= 2.5
    expected3 = str(Fx("10.0"))
    actual3 = str(x3)
    cprint(f'x = Fx("4"); x *= 2.5; x = {actual3}', "cyan")

    x4 = Fx("9")
    x4 //= 2
    expected4 = str(Fx("4.0"))
    actual4 = str(x4)
    cprint(f'x = Fx("9"); x //= 2; x = {actual4}', "cyan")

    cprint('-'*40, as_="bold white")

    if actual1 == expected1:
        pass_local += 1
    if actual2 == expected2:
        pass_local += 1
    if actual3 == expected3:
        pass_local += 1
    if actual4 == expected4:
        pass_local += 1

    test_count += 1
    if pass_local == total_local:
        pass_count += 1
        cprint(f"Pass, {pass_local} out of {total_local}", as_="bold green")
    else:
        cprint(f"Fail, {pass_local} out of {total_local}", as_="bold red")

    print()


    cprint("="*40, as_="bold white")
    cprint(f"TOTAL: {pass_count} out of {test_count} test containers passed", as_="bold white on black")
    if pass_count == test_count:
        cprint("ALL TEST CONTAINERS PASSED!", as_="bold green")
    else:
        cprint(f"{test_count - pass_count} test containers failed", as_="bold red")
    cprint("="*40, as_="bold white")
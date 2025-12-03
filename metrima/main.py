from .fx import Fx, fx

def _make_divider(divisor: str = "-",
                  count: int = 60) -> str:
    return divisor*count

def add(a: int | float | Fx,
        b: int | float | Fx) -> int | float | Fx:
    """
    Add two numbers
    :param a:
    :param b:
    :return:
    """
    if isinstance(a, float):
        a = fx(a)
    if isinstance(b, float):
        b = fx(b)
    return a + b

def subtract(a: int | float | Fx,
             b: int | float | Fx) -> int | float | Fx:
    """
    Subtract two numbers
    :param a:
    :param b:
    :return:
    """
    if isinstance(a, float):
        a = fx(a)
    if isinstance(b, float):
        b = fx(b)
    return a - b

def mul(a: int | float | Fx,
        b: int | float | Fx) -> int | float | Fx:
    """
    Multiply two numbers
    :param a:
    :param b:
    :return:
    """
    if isinstance(a, float):
        a = fx(a)
    if isinstance(b, float):
        b = fx(b)
    return a * b

def div(a: int | float | Fx,
        b: int | float | Fx) -> int | float | Fx:
    """
    Divide two numbers
    :param a:
    :param b:
    :return:
    """
    if isinstance(a, float):
        a = fx(a)
    if isinstance(b, float):
        b = fx(b)
    if b != 0:
        return a / b
    raise ZeroDivisionError


def sigma(collection: list[Fx] | list[int] | list[float]) -> Fx:
    return_result = 0
    for i in collection:
        return_result += i
    return return_result

def sigma_noiter(*numbers: Fx | int | float) -> Fx:
    return_result = Fx(0)
    for i in numbers:
        i = fx(i)
        return_result += i
    return return_result

def power(base: int | float | Fx,
        exp: int | float | Fx) -> int | float | Fx:
    if isinstance(base, (int, float)):
        base = fx(base)
    if isinstance(exp, (int, float)):
        exp = fx(exp)
    return base ** exp

if __name__ == "__main__":
    from tests import test_main
    test_main()

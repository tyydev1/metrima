from fx import Fx, fx

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
    if a != 0:
        return a / b
    raise ZeroDivisionError

if __name__ == "__main__":
    from tests import test_main
    test_main()

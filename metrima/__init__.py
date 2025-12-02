from tinycolors import colortext, color, clib, cprint
from fx import Fx

def add(a: int | float | Fx, b: int | float) -> int | float:
    return a + b

def subtract(a: int | float, b: int | float) -> int | float:
    return a - b

def mul(a: int | float, b: int | float) -> int | float:
    return a * b

def div(a: int | float, b: int | float) -> int | float:
    if a != 0:
        return a / b
    raise ZeroDivisionError

def test() -> None:
    """
    Test demo for Metrima
    :return:
    """
    cprint('='*60, as_="bold white")
    cprint("             Metrima v0.0.1 Testing Grounds              ", as_="bold white")
    cprint("Welcome to Metrima! A small, comprehensive math library. ", as_="bold white")
    cprint('='*60, as_="bold white")

    cprint("Addition", as_="bold yellow")
    cprint("1.432 + 5.1234 is..", as_="bold yellow")
    actual = add(Fx(1.432), Fx(5.1234))
    expected = 6.5554

    cprint('- '*30, as_="bold white")
    cprint("Metrima says: ", as_="bold blue")

    print(f"{color.bg.black}{color.dim}{color.italic}{actual}{clib.reset}")

    cprint('- '*30, as_="bold white")
    cprint("What we expected: ", as_="bold blue")
    cprint(f"{color.italic}6.5554", as_="bold green on black")

    cprint('- '*30, as_="bold white")
    cprint("Metrima is..", as_="bold blue", end=" ")
    if actual == expected:
        cprint(f"{color.bold}CORRECT!", as_="italic green")
        cprint(f"{actual} is {expected}", as_="italic green")
    else:
        cprint(f"{color.bold}INCORRECT!", as_="italic red")
        cprint(f"{actual} is NOT {expected}", color="red")

    print()

    cprint('-'*60, as_="bold white")

if __name__ == "__main__":
    test()

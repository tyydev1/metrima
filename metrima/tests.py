from tinycolors import cprint, color, clib, cinput
from main import _make_divider
from fx import Fx, fx
from custerror import MissingArgument
from decimal import Decimal


def _create_test(title: str,
                 action: str,
                 expected: int | float,
                 actual: int | float | Fx,
                 _python: int | float | None = None,
                 _show_actual_python: bool = False,
                 _show_divisor: bool = True,
                 _decimal: Decimal | None = None,
                 _show_actual_decimal: bool = False) -> bool | tuple[bool, bool] | tuple[bool, bool, bool]:
    if _python is None and _show_actual_python:
        raise MissingArgument(f"Missing argument for '{_create_test.__name__}': '_python'")
    if _decimal is None and _show_actual_decimal:
        raise MissingArgument(f"Missing argument for '{_create_test.__name__}': '_decimal'")

    cprint(f"{title}", as_="bold yellow")
    cprint(f"{action} is...", as_="bold yellow")

    cprint(_make_divider('- ', 30), as_="bold white")
    cprint("Metrima says: ", as_="bold blue")
    print(f"{color.bg.black}{color.dim}{color.italic}{actual}{clib.reset}")

    cprint(_make_divider('- ', 30), as_="bold white")
    cprint("What we expected: ", as_="bold blue")
    cprint(f"{color.italic}{expected}", as_="bold green on black")

    cprint(_make_divider('- ', 30), as_="bold white")
    cprint("Metrima is..", as_="bold blue", end=" ")
    if actual == expected:
        cprint(f"{color.bold}CORRECT!", as_="italic green")
        cprint(f"{actual} is {expected}", as_="italic green")
    else:
        cprint(f"{color.bold}INCORRECT!", as_="italic red")
        cprint(f"{actual} is NOT {expected}", color="red")

    print()

    if not _show_actual_python and not _show_actual_decimal:
        cprint(_make_divider('='), as_="bold white") if _show_divisor else None
        return actual == expected

    if _show_actual_python:
        cprint("What Python says:", as_="bold cyan")
        _color = "bold red on black" if _python != expected else "bold green on black"
        cprint(f"{color.italic}{_python}", as_=_color)
        print()

    if _show_actual_decimal:
        cprint("What Decimal says:", as_="bold magenta")
        _decimal_float = float(_decimal)
        _color = "bold red on black" if _decimal_float != expected else "bold green on black"
        cprint(f"{color.italic}{_decimal}", as_=_color)

    cprint(_make_divider('='), as_="bold white") if _show_divisor else None

    if _show_actual_python and _show_actual_decimal:
        return actual == expected, _python == expected, _decimal_float == expected
    elif _show_actual_python:
        return actual == expected, _python == expected
    else:
        return actual == expected


def test_main() -> None:
    """
    Test demo for Metrima
    :return:
    """
    cprint(_make_divider('='), as_="bold white")
    cprint("             Metrima v0.1.0 Testing Grounds             ", as_="bold white")
    cprint("        Metrima Demo, Metrima VS Python VS Decimal      ", as_="bold white")
    cprint(_make_divider('='), as_="bold white")
    total = 0
    passed = 0
    pytotal = 0
    pypassed = 0
    dectotal = 0
    decpassed = 0

    # -- ADDITION -- #
    result = _create_test("Addition", "1.432 + 5.1234", 6.5554,
                          fx(1.432) + fx(5.1234),
                          1.432 + 5.1234, True,
                          True,
                          Decimal('1.432') + Decimal('5.1234'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- SUBTRACTION -- #
    result = _create_test("Subtraction", "10.0 - 2.45", 7.55,
                          fx(10.0) - fx(2.45),
                          10.0 - 2.45, True,
                          True,
                          Decimal('10.0') - Decimal('2.45'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- MULTIPLICATION -- #
    result = _create_test("Multiplication", "7.2 * 41.512", 298.8864,
                          fx(7.2) * fx(41.512),
                          7.2 * 41.512, True,
                          True,
                          Decimal('7.2') * Decimal('41.512'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- DIVISION -- #
    result = _create_test("Division", "3.6 / 1.2", 3.0,
                          fx(3.6) / fx(1.2),
                          3.6 / 1.2, True,
                          True,
                          Decimal('3.6') / Decimal('1.2'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- POWER/EXPONENTIATION -- #
    result = _create_test("Power", "2.5 ** 3", 15.625,
                          fx(2.5) ** fx(3),
                          2.5 ** 3, True,
                          True,
                          Decimal('2.5') ** Decimal('3'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- MODULO -- #
    result = _create_test("Modulo", "10.5 % 3.2", 0.9,
                          fx(10.5) % fx(3.2),
                          10.5 % 3.2, True,
                          True,
                          Decimal('10.5') % Decimal('3.2'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- FLOOR DIVISION -- #
    result = _create_test("Floor Division", "17.8 // 4.0", 4.0,
                          fx(17.8) // fx(4.0),
                          17.8 // 4.0, True,
                          True,
                          Decimal('17.8') // Decimal('4.0'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- NEGATION -- #
    result = _create_test("Negation", "-(-5.75)", 5.75,
                          -fx(-5.75),
                          -(-5.75), True,
                          True,
                          -(-Decimal('5.75')), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- ABSOLUTE VALUE -- #
    result = _create_test("Absolute Value", "abs(-12.345)", 12.345,
                          abs(fx(-12.345)),
                          abs(-12.345), True,
                          True,
                          abs(Decimal('-12.345')), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- COMPLEX EXPRESSION -- #
    result = _create_test("Complex Expression", "(2.5 + 3.5) * 4 - 10 / 2", 19.0,
                          (fx(2.5) + fx(3.5)) * fx(4) - fx(10) / fx(2),
                          (2.5 + 3.5) * 4 - 10 / 2, True,
                          True,
                          (Decimal('2.5') + Decimal('3.5')) * Decimal('4') - Decimal('10') / Decimal('2'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- CHAINED OPERATIONS -- #
    result = _create_test("Chained Addition", "1.1 + 2.2 + 3.3 + 4.4", 11.0,
                          fx(1.1) + fx(2.2) + fx(3.3) + fx(4.4),
                          1.1 + 2.2 + 3.3 + 4.4, True,
                          True,
                          Decimal('1.1') + Decimal('2.2') + Decimal('3.3') + Decimal('4.4'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # -- MIXED OPERATIONS -- #
    result = _create_test("Mixed Operations", "5 * 3 + 12 / 4 - 2", 16.0,
                          fx(5) * fx(3) + fx(12) / fx(4) - fx(2),
                          5 * 3 + 12 / 4 - 2, True, False,
                          Decimal('5') * Decimal('3') + Decimal('12') / Decimal('4') - Decimal('2'), True)
    total += 1
    pytotal += 1
    dectotal += 1
    passed += result[0]
    pypassed += result[1]
    decpassed += result[2]

    # Summary
    cprint("\n" + _make_divider('='), as_="bold white")
    cprint("                    TESTING COMPLETE!                    ", as_="bold green")
    cprint(_make_divider('='), as_="bold white")

    text_color = "bold cyan" if passed != total else "bold blue"
    cprint(f"\nMetrima Results: {passed}/{total} tests passed", as_=text_color)
    metrima_percentage = (passed / total * 100) if total > 0 else 0
    metrima_color = "bold green" if passed == total else "bold yellow" if passed > total * 0.5 else "bold red"
    cprint(f"Success Rate: {metrima_percentage:.1f}%", as_=metrima_color)

    text_color = "bold cyan" if pypassed != total else "bold magenta"
    cprint(f"\nPython Results: {pypassed}/{pytotal} tests passed", as_=text_color)
    python_percentage = (pypassed / pytotal * 100) if pytotal > 0 else 0
    python_color = "bold green" if pypassed == pytotal else "bold yellow" if pypassed > pytotal * 0.5 else "bold red"
    cprint(f"Success Rate: {python_percentage:.1f}%", as_=python_color)

    text_color = "bold cyan" if decpassed != total else "bold magenta"
    cprint(f"\nDecimal Results: {decpassed}/{dectotal} tests passed", as_=text_color)
    decimal_percentage = (decpassed / dectotal * 100) if dectotal > 0 else 0
    decimal_color = "bold green" if decpassed == dectotal else "bold yellow" if decpassed > dectotal * 0.5 else "bold red"
    cprint(f"Success Rate: {decimal_percentage:.1f}%", as_=decimal_color)

    cprint("\n" + _make_divider('='), as_="bold white")

def test_fx():
    cprint(_make_divider('='), as_="bold white")
    cprint("             Metrima v0.1.0 Testing Grounds             ", as_="bold white")
    cprint(f"       Metrima's {color.bg.black}Fx{clib.reset} testing      ", as_="bold white")
    cprint(_make_divider('='), as_="bold white")
    print()

    test_count = 0
    pass_count = 0

    cprint("Fx class testing", as_="bold white on black")
    print()


    pass_local = 0
    total_local = 6

    cprint("repr(Fx()) and str(Fx())", as_="bold yellow")
    cprint('-'*40, as_="bold white")

    expected1, expected2, expected3 = 'Fx(value=0, scale=0)', 'Fx(value=0, scale=0)', 'Fx(value=0, scale=0)'
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

    expected2 = str(Fx("1"))
    actual2 = str(Fx(7) % 3)
    cprint(f'Fx(7) % 3 = {actual2}', "cyan")

    expected3 = str(Fx("0"))
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
        cprint("ALL TEST CONTAINERS PASS", as_="bold green")
    else:
        cprint(f"{test_count - pass_count} test containers failed", as_="bold red")
    cprint("="*40, as_="bold white")

def menu():
    cprint(_make_divider('='), as_="bold white")
    cprint("             Metrima v0.1.0 Testing Grounds              ", as_="bold white")
    cprint(" Welcome to Metrima! A small, comprehensive math library.", as_="bold white")
    cprint(_make_divider('='), as_="bold white")

    print()
    cprint(f'{color.italic}1. Competition Demo', as_="bold bright red")
    cprint('2. Fx Class Testing', as_="italic blue")
    user_choice = cinput(f"{color.italic}Which test would you like to run? ", as_="dim default")
    print()

    _make_divider()
    if user_choice in ["1", "competition", "c", "comp", "main"]:
        test_main()
    elif user_choice in ["2", "fx"]:
        test_fx()
    elif user_choice in ["quit", "exit", "q", "x"]:
        exit(0)
    else:
        cprint('x Invalid choice', as_="bold red")

if __name__ == "__main__":
    menu()
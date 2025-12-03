
# Metrima

A small, comprehensive math library with fixed-point arithmetic precision.

## Overview

Metrima is a Python math library that implements the `Fx` (Fixed-point) class to provide precise decimal arithmetic without the floating-point precision issues common in standard Python operations.

## Features

- **Fixed-Point Arithmetic**: Avoid floating-point precision errors
- **Full Operator Support**: All standard math operations (+, -, *, /, //, %, **)
- **Type Conversions**: Seamless conversion between `Fx`, `int`, `float`, and `str`
- **Comparison Operations**: Complete set of comparison operators
- **In-place Operations**: Support for `+=`, `-=`, `*=`, etc.
- **Unary Operations**: Negation, absolute value, and rounding

## Installation

```bash
pip install metrima
```

## Quick Start

```python
from metrima import Fx, fx

# Create fixed-point numbers
a = Fx("1.432")
b = fx(5.1234)  # Convenience function

# Perform arithmetic
result = a + b
print(result)  # 6.5554

# Mix with regular numbers
c = Fx(10.0) - 2.45
print(c)  # 7.55

# Complex expressions
d = (Fx(2.5) + Fx(3.5)) * Fx(4) - Fx(10) / Fx(2)
print(d)  # 19.0
```

## Why Metrima?

Standard Python floating-point arithmetic can produce unexpected results:

```python
# Python's float arithmetic
0.1 + 0.2  # 0.30000000000000004 😱

# Metrima's Fx arithmetic
Fx(0.1) + Fx(0.2)  # 0.3 ✨
```

## The Fx Class

The `Fx` class stores numbers as scaled integers, maintaining precision by tracking the decimal scale separately.

### Creating Fx Objects

```python
# From string (recommended for decimals)
x = Fx("3.14159")

# From int
y = Fx(42)

# From float
z = Fx(2.5)

# Using the fx() convenience function
w = fx("1.23")
```

### Arithmetic Operations

```python
a = Fx("10.5")
b = Fx("2.5")

a + b   # Addition: 13.0
a - b   # Subtraction: 8.0
a * b   # Multiplication: 26.25
a / b   # Division: 4.2
a // b  # Floor division: 4.0
a % b   # Modulo: 0.5
a ** 2  # Power: 110.25
```

### Comparisons

```python
Fx("2.0") == Fx("2")    # True
Fx(3) != 3              # False
Fx("1.5") > Fx("1.4")   # True
Fx("1.2") < 2           # True
```

### Type Conversions

```python
x = Fx("3.14")

float(x)  # 3.14
int(x)    # 3
str(x)    # "3.14"
bool(x)   # True
```

## Testing

Metrima includes comprehensive test suites comparing its accuracy against both standard Python arithmetic and Python's `Decimal` class.

### Run Interactive Tests

```bash
metrimatest
```

This launches an interactive menu where you can choose:
1. **Competition Demo** - Compare Metrima vs Python vs Decimal
2. **Fx Class Testing** - Detailed unit tests for the Fx class

### Test from Code

```python
from metrima import test_main

test_main()  # Run the full test suite
```

## API Reference

### Basic Functions

```python
from metrima import add, subtract, mul, div

add(a, b)       # Addition
subtract(a, b)  # Subtraction
mul(a, b)       # Multiplication
div(a, b)       # Division
```

### Fx Methods

- `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
- `__neg__`, `__pos__`, `__abs__`, `__round__`
- `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
- `__int__`, `__float__`, `__str__`, `__repr__`, `__bool__`

## Requirements

- Python >= 3.14
- `tinycolors` (for colorized test output)

## Version

Current version: **0.2.0**

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

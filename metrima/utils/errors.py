class UnexpectedTypeError(Exception):
    pass

class MissingArgument(Exception):
    pass

class ConstantError(Exception):
    def __init__(self, message: str = "Cannot modify a constant") -> None:
        super().__init__(message)

class DimensionError(Exception):
    """
    Custom error raised when an invalid unit conversion is attempted.
    """

    def __init__(self, unit_a, unit_b, message: str = None):
        self.unit_a = unit_a
        self.unit_b = unit_b

        class_a = type(unit_a).__name__
        class_b = type(unit_b).__name__

        if message is None:
            message = (
                f"Attempted to execute an operation between incompatible unit dimensions: "
                f"'{class_a}' and '{class_b}'. "
                f"Check that both units belong to the same system (Weight, Distance, Time, Temperature) "
            )

        super().__init__(message)
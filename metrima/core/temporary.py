from typing import Any

class Temporary:
    def __init__(self, value: Any):
        super().__setattr__("_Temporary__value", value)

    def __getattribute__(self, name: str) -> Any:
        try:
            value = super().__getattribute__("_Temporary__value")
        except AttributeError:
            raise AttributeError("Wrapped object is gone (accessed Temporary value once)")

        if value is None:
            raise AttributeError("Wrapped object is gone (accessed Temporary value once)")

        super().__setattr__("_Temporary__value", None)

        if name == "value":
            return value
        else:
            return getattr(value, name)

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify a Temporary object")

    def __delattr__(self, name):
        raise AttributeError("Cannot delete attributes of a Temporary object")

    def __str__(self):
        return f"{self.value}"

def temp(value: Any) -> Temporary:
    return Temporary(value)
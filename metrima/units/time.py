from typing import Optional, Union
import warnings

from metrima.core.fx import Fx

Numeric = Union[int, float]

class TimeUnit:
    """
    Base class for all time units (Hour, Minute, Second, Millisecond).
    """
    raw_value: Union[int, 'TimeUnit', float]
    value: int

    def __init__(self, value: Union[int, 'Hour', 'Minute', 'Second', 'Millisecond', float]) -> None:
        """
        Initializes a TimeUnit instance with the provided value.
        Upon initialization, it calls the _process_value method to handle the input appropriately.
        Following the SI convention, time units will default to seconds unless specified otherwise by subclass.

        :param self: The instance of the TimeUnit class.
        :param value: The value representing the time unit, which can be an integer or another TimeUnit subclass instance.
        :type value: int | 'Hour' | 'Minute' | 'Second' | 'Millisecond'
        """
        self.raw_value = value

        self._process_value()

    def _process_value(self) -> None:
        """
        **Abstract Method:** This method is intended to be overridden by subclasses 
        to handle the input value in a way specific to the time unit (Hour, Minute, etc.).
        
        If a concrete class forgets to implement this, it will raise a NotImplementedError.
        """
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must implement the {self._process_value.__name__} method."
        )
    
    def __second__(self) -> int:
        """
        Type casting to seconds. second(self)
        
        :param self: The instance of the class
        """
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must implement the {self.__second__.__name__} method."
        )
    
    def __minute__(self) -> int:
        """
        Type casting to minutes. minute(self)
        
        :param self: The instance of the class
        """
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must implement the {self.__minute__.__name__} method."
        )
    
    def __hour__(self) -> int:
        """
        Type casting to hours. hour(self)
        
        :param self: The instance of the class
        """
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must implement the {self.__hour__.__name__} method."
        )
    
    def __millisecond__(self) -> int:
        """
        Type casting to milliseconds. ms(self)

        :param self: The instance of the class
        """
        raise NotImplementedError(
            f"Subclass {self.__class__.__name__} must implement the {self.__millisecond__.__name__} method."
        )
    
    def __add__(self, other: Union[int, float, 'TimeUnit']) -> 'Second':
        """Add two TimeUnit values and return a Second instance (SI base).

        - If `other` is a TimeUnit, both are converted to milliseconds, summed,
          and returned as `Second(total_ms / 1000)` so fractional seconds are
          preserved and processed by `Second` class.
        - If `other` is numeric, it is interpreted as seconds.
        """
        if isinstance(other, TimeUnit):
            total_ms = self.__millisecond__() + other.__millisecond__()
        elif isinstance(other, (int, float)):
            total_ms = self.__millisecond__() + int(float(other) * 1000)
        else:
            return NotImplemented

        return second(total_ms / 1000)

    def __radd__(self, other: Union[int, float, 'TimeUnit']) -> 'Second':
        """Right-side addition to support numeric + TimeUnit."""
        return self.__add__(other)

    def __sub__(self, other: Union[int, float, 'TimeUnit']) -> 'Second':
        """Subtract and return a `Second` instance (SI base)."""
        if isinstance(other, TimeUnit):
            total_ms = self.__millisecond__() - other.__millisecond__()
        elif isinstance(other, (int, float)):
            total_ms = self.__millisecond__() - int(float(other) * 1000)
        else:
            return NotImplemented

        return second(total_ms / 1000)

    def __rsub__(self, other: Union[int, float, 'TimeUnit']) -> 'Second':
        """Right-side subtraction: numeric - TimeUnit or TimeUnit - TimeUnit."""
        if isinstance(other, TimeUnit):
            total_ms = other.__millisecond__() - self.__millisecond__()
        elif isinstance(other, (int, float)):
            total_ms = int(float(other) * 1000) - self.__millisecond__()
        else:
            return NotImplemented

        return second(total_ms / 1000)

    def __mul__(self, other: Union[int, float]) -> 'Second':
        """Scale a time value by a numeric factor, returning `Second`."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        total_ms = int(self.__millisecond__() * float(other))
        return second(total_ms / 1000)

    def __rmul__(self, other: Union[int, float]) -> 'Second':
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float, 'TimeUnit']):
        """Division operator.

        - If dividing by a numeric, returns a `Second` scaled down.
        - If dividing by another TimeUnit, returns a float ratio (self/other).
        """
        if isinstance(other, TimeUnit):
            other_ms = other.__millisecond__()
            if other_ms == 0:
                raise ZeroDivisionError("division by zero TimeUnit")
            return self.__millisecond__() / other_ms
        if isinstance(other, (int, float)):
            if float(other) == 0:
                raise ZeroDivisionError("division by zero")
            total_ms = int(self.__millisecond__() / float(other))
            return second(total_ms / 1000)
        return NotImplemented

    def __rtruediv__(self, other: Union[int, float]):
        """Right division: numeric / TimeUnit -> ratio (float)."""
        if not isinstance(other, (int, float)):
            return NotImplemented
        denom = self.__millisecond__()
        if denom == 0:
            raise ZeroDivisionError("division by zero TimeUnit")
        return (float(other) * 1000) / denom

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TimeUnit):
            return self.__millisecond__() == other.__millisecond__()
        if isinstance(other, (int, float)):
            return self.__millisecond__() == int(float(other) * 1000)
        return NotImplemented

    def __lt__(self, other: Union[int, float, 'TimeUnit']) -> bool:
        if isinstance(other, TimeUnit):
            return self.__millisecond__() < other.__millisecond__()
        if isinstance(other, (int, float)):
            return self.__millisecond__() < int(float(other) * 1000)
        return NotImplemented

    def __le__(self, other: Union[int, float, 'TimeUnit']) -> bool:
        return self == other or self < other

    def __gt__(self, other: Union[int, float, 'TimeUnit']) -> bool:
        return not self <= other

    def __ge__(self, other: Union[int, float, 'TimeUnit']) -> bool:
        return not self < other


class Hour(TimeUnit):
    """
    Hour-specific time unit.
    """
    minutes: Optional[Union[int, Fx]] = None
    seconds: Optional[Union[int, Fx]] = None
    milliseconds: Optional[Union[int, Fx]] = None

    def _process_value(self) -> None:
        """
        Hour-specific logic for processing the input value.
        
        :param self: The instance of the Hour class.
        """
        allowed: list = [TimeUnit, int, float]
        if not isinstance(self.raw_value, tuple(allowed)):
            raise TypeError(
                "Hours can only be instantiated from another TimeUnit instance or a numeric type."
            )
        
        raw: Union[int, float, TimeUnit] = self.raw_value

        if isinstance(raw, int):
            self.value: int = raw
            return
        
        if isinstance(raw, float):
            from metrima.units.utils import downgrade_float_fx
            chain = [(60, "minutes"), (60, "seconds"), (1000, "milliseconds")]
            whole, leftover = downgrade_float_fx(raw, chain)

            CONVERSION_FACTOR = 3_600_000

            if leftover is None:
                self.value = whole // CONVERSION_FACTOR
            else:
                unit_name, val_fx = leftover
                warnings.warn(
                    f"Float value stored in {unit_name} and truncated for calculations",
                    UserWarning
                )
                setattr(self, unit_name, val_fx)
                self.value = whole // CONVERSION_FACTOR
                    
        if isinstance(raw, TimeUnit):
            total_ms = raw.__millisecond__()
            self.value = total_ms // 3_600_000
            remaining_ms = total_ms % 3_600_000
            
            if remaining_ms >= 60_000:
                self.minutes = remaining_ms // 60_000
                remaining_ms %= 60_000
            
            if remaining_ms >= 1000:
                self.seconds = remaining_ms // 1000
                remaining_ms %= 1000
            
            if remaining_ms > 0:
                self.milliseconds = remaining_ms

    def __minute__(self) -> int:
        total_minutes = self.value * 60
        if self.minutes is not None:
            total_minutes += int(self.minutes)
        if self.seconds is not None:
            total_minutes += int(self.seconds) // 60
        if self.milliseconds is not None:
            total_minutes += int(self.milliseconds) // 60_000
        return total_minutes

    def __second__(self) -> int:
        total_seconds = self.value * 3600
        if self.minutes is not None:
            total_seconds += int(self.minutes) * 60
        if self.seconds is not None:
            total_seconds += int(self.seconds)
        if self.milliseconds is not None:
            total_seconds += int(self.milliseconds) // 1000
        return total_seconds
    
    def __millisecond__(self) -> int:
        total_ms = self.value * 3_600_000
        if self.minutes is not None:
            total_ms += int(self.minutes) * 60_000
        if self.seconds is not None:
            total_ms += int(self.seconds) * 1000
        if self.milliseconds is not None:
            total_ms += int(self.milliseconds)
        return total_ms
    
    def __hour__(self) -> int:
        return self.value
    
    def __repr__(self) -> str:
        return f"Hour({self.value})"
    
    def __str__(self) -> str:
        parts = [f"{self.value}h"]
        if self.minutes is not None:
            parts.append(f"{int(self.minutes)}m")
        if self.seconds is not None:
            parts.append(f"{int(self.seconds)}s")
        if self.milliseconds is not None:
            parts.append(f"{int(self.milliseconds)}ms")
        return " ".join(parts)


class Minute(TimeUnit):
    """
    Minute-specific time unit.
    """
    seconds: Optional[Union[int, Fx]] = None
    milliseconds: Optional[Union[int, Fx]] = None

    def _process_value(self) -> None:
        """
        Minute-specific logic for processing the input value.
        
        :param self: The instance of the Minute class.
        """
        allowed: list = [TimeUnit, int, float]
        if not isinstance(self.raw_value, tuple(allowed)):
            raise TypeError(
                "Minutes can only be instantiated from another TimeUnit instance or a numeric type."
            )
        
        raw: Union[int, float, TimeUnit] = self.raw_value
        
        if isinstance(raw, int):
            self.value: int = raw
            return
            
        if isinstance(raw, float):
            from metrima.units.utils import downgrade_float_fx
            chain = [(60, "seconds"), (1000, "milliseconds")]
            whole, leftover = downgrade_float_fx(raw, chain)

            CONVERSION_FACTOR = 60_000
            self.value = whole // CONVERSION_FACTOR
            if leftover is not None:
                unit_name, val_fx = leftover
                warnings.warn(
                    f"Float value stored in {unit_name} and truncated for calculations",
                    UserWarning
                )
                setattr(self, unit_name, val_fx)

        if isinstance(raw, TimeUnit):
            total_ms = raw.__millisecond__()
            self.value = total_ms // 60_000
            remaining_ms = total_ms % 60_000
            
            if remaining_ms >= 1000:
                self.seconds = remaining_ms // 1000
                remaining_ms %= 1000
            
            if remaining_ms > 0:
                self.milliseconds = remaining_ms

    def __hour__(self) -> int:
        total_minutes = self.value
        if self.seconds is not None:
            total_minutes += int(self.seconds) // 60
        if self.milliseconds is not None:
            total_minutes += int(self.milliseconds) // 60_000
        return total_minutes // 60
    
    def __minute__(self) -> int:
        return self.value

    def __second__(self) -> int:
        total_seconds = self.value * 60
        if self.seconds is not None:
            total_seconds += int(self.seconds)
        if self.milliseconds is not None:
            total_seconds += int(self.milliseconds) // 1000
        return total_seconds
    
    def __millisecond__(self) -> int:
        total_ms = self.value * 60_000
        if self.seconds is not None:
            total_ms += int(self.seconds) * 1000
        if self.milliseconds is not None:
            total_ms += int(self.milliseconds)
        return total_ms
    
    def __repr__(self) -> str:
        return f"Minute({self.value})"
    
    def __str__(self) -> str:
        parts = [f"{self.value}m"]
        if self.seconds is not None:
            parts.append(f"{int(self.seconds)}s")
        if self.milliseconds is not None:
            parts.append(f"{int(self.milliseconds)}ms")
        return " ".join(parts)


class Second(TimeUnit):
    """
    Second-specific time unit.
    """
    milliseconds: Optional[Union[int, Fx]] = None

    def _process_value(self) -> None:
        """
        Second-specific logic for processing the input value.
        
        :param self: The instance of the Second class.
        """
        allowed: list = [TimeUnit, int, float]
        if not isinstance(self.raw_value, tuple(allowed)):
            raise TypeError(
                "Seconds can only be instantiated from another TimeUnit instance or a numeric type."
            )

        raw: Union[int, float, TimeUnit] = self.raw_value
        
        if isinstance(raw, int):
            self.value: int = raw
            return
            
        if isinstance(raw, float):
            from metrima.units.utils import downgrade_float_fx
            chain = [(1000, "milliseconds")]
            whole, leftover = downgrade_float_fx(raw, chain)

            CONVERSION_FACTOR = 1000
            self.value = whole // CONVERSION_FACTOR
            remainder = whole % CONVERSION_FACTOR
            if remainder:
                self.milliseconds = remainder
                warnings.warn(
                    "Float value had millisecond remainder; stored in .milliseconds",
                    UserWarning
                )
            if leftover is not None:
                unit_name, val_fx = leftover
                warnings.warn(
                    f"Float value stored in {unit_name} and truncated for calculations",
                    UserWarning
                )
                setattr(self, unit_name, val_fx)

        if isinstance(raw, TimeUnit):
            total_ms = raw.__millisecond__()
            self.value = total_ms // 1000
            remaining_ms = total_ms % 1000
            
            if remaining_ms > 0:
                self.milliseconds = remaining_ms

    def __hour__(self) -> int:
        total_seconds = self.value
        if self.milliseconds is not None:
            total_seconds += int(self.milliseconds) // 1000
        return total_seconds // 3_600

    def __minute__(self) -> int:
        total_seconds = self.value
        if self.milliseconds is not None:
            total_seconds += int(self.milliseconds) // 1000
        return total_seconds // 60
    
    def __second__(self) -> int:
        return self.value
    
    def __millisecond__(self) -> int:
        total_ms = self.value * 1000
        if self.milliseconds is not None:
            total_ms += int(self.milliseconds)
        return total_ms
    
    def __repr__(self) -> str:
        return f"Second({self.value})"
    
    def __str__(self) -> str:
        parts = [f"{self.value}s"]
        if self.milliseconds is not None:
            parts.append(f"{int(self.milliseconds)}ms")
        return " ".join(parts)


class Millisecond(TimeUnit):
    """
    Millisecond-specific time unit.
    """
    
    def _process_value(self) -> None:
        """
        Millisecond-specific logic for processing the input value.
        
        :param self: The instance of the Millisecond class.
        """
        if not isinstance(self.raw_value, (TimeUnit, int, float)):
            raise TypeError(
                "Milliseconds can only be instantiated from another TimeUnit instance or a numeric type."
            )
        
        if isinstance(self.raw_value, float):
            warnings.warn(
                "Float values are not supported for milliseconds because it is the lowest unit implemented. Converting to int by truncation.",
                UserWarning
            )
            self.raw_value = int(self.raw_value)

        if isinstance(self.raw_value, int):
            self.value = self.raw_value
        else:
            self.value = self.raw_value.__millisecond__()

    def __hour__(self) -> int:
        return self.value // 3_600_000
    
    def __minute__(self) -> int:
        return self.value // 60_000
    
    def __second__(self) -> int:
        return self.value // 1000
    
    def __millisecond__(self) -> int:
        return self.value
    
    def __repr__(self) -> str:
        return f"Millisecond({self.value})"
    
    def __str__(self) -> str:
        return f"{self.value}ms"


def second(value: Union[int, float, 'Second', 'Hour', 'Minute', 'Millisecond']) -> Second:
    """
    Converts the given value to seconds, if possible.
    
    :param value: Value to convert to seconds
    :type value: int | float | 'Second' | 'Hour' | 'Minute' | 'Millisecond'
    :return: Second instance
    :rtype: Second
    """
    return Second(value)


def minute(value: Union[int, float, 'Second', 'Hour', 'Minute', 'Millisecond']) -> Minute:
    """
    Converts the given value to minutes, if possible.
    
    :param value: Value to convert to minutes
    :type value: int | float | 'Second' | 'Hour' | 'Minute' | 'Millisecond'
    :return: Minute instance
    :rtype: Minute
    """
    return Minute(value)


def hour(value: Union[int, float, 'Second', 'Hour', 'Minute', 'Millisecond']) -> Hour:
    """
    Converts the given value to hours, if possible.
    
    :param value: Value to convert to hours
    :type value: int | float | 'Second' | 'Hour' | 'Minute' | 'Millisecond'
    :return: Hour instance
    :rtype: Hour
    """
    return Hour(value)


def ms(value: Union[int, float, 'Second', 'Hour', 'Minute', 'Millisecond']) -> Millisecond:
    """
    Converts the given value to milliseconds, if possible.
    
    :param value: Value to convert to milliseconds
    :type value: int | float | 'Second' | 'Hour' | 'Minute' | 'Millisecond'
    :return: Millisecond instance
    :rtype: Millisecond
    """
    if isinstance(value, (int, float)):
        return Millisecond(int(value))
    else:
        return Millisecond(value)
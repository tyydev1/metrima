from metrima.core.fx import Fx
from metrima.lib import is_whole
from typing import List, Tuple, Optional

def downgrade_float_fx(value: float, chain: List[Tuple[int, str]]) -> Tuple[int, Optional[Tuple[str, Fx]]]:
    """
    Downgrades a float through a chain of conversion factors until we get a whole number.
    
    :param value: Original float value.
    :param chain: List of (factor, unit_name) tuples, e.g., [(60, "minutes"), (60, "seconds"), (1000, "milliseconds")].
    :return: (whole_value: int, leftover: Optional[Tuple[str, Fx]]).
    """
    current_val = Fx(value)
    
    for i, (factor, unit_name) in enumerate(chain):
        current_val *= Fx(factor)
        
        if is_whole(current_val):
            remaining_chain = chain[i+1:]
            for next_factor, _ in remaining_chain:
                current_val *= Fx(next_factor)
            return int(current_val), None
            
    return int(current_val), (unit_name, current_val)


class MetricUnit:
    """This is a Metric unit."""
    pass

class ImperialUnit:
    """
    This is an Imperial unit.
    """
    pass
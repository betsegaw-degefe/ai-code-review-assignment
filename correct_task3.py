import math
from typing import List, Any, Optional

def average_valid_measurements(values: Optional[List[Any]]) -> float:
    """
    Calculate the average of valid numeric measurements from a list, excluding None and invalid values.
    
    Args:
        values: A list of values (can be None, non-iterable, or contain mixed types).
               Valid measurements are numeric types (int, float, including negative numbers)
               or strings that can be converted to float. Can be None or non-iterable,
               in which case returns 0.0.
    
    Returns:
        float: The average of valid measurements. Returns 0.0 if input is None, non-iterable,
               empty, or contains no valid measurements.
    
    Notes:
        - Excludes None values, boolean values, infinity, NaN, and values that can't convert to float
        - Accepts numeric types (int, float) and string representations of numbers (including negative numbers)
        - Safely handles edge cases: None input, non-iterable input, invalid types, empty lists
        - Invalid entries (None, bool, complex, infinity, NaN, non-convertible strings) are skipped
    """
    if values is None:
        return 0.0
    
    try:
        iter(values)
    except TypeError:
        return 0.0
    
    total = 0
    count = 0

    for v in values:
        if v is not None:
            # Exclude bool explicitly (bool can convert to float but shouldn't be included)
            if isinstance(v, bool):
                continue
            # Check if value is numeric (int or float)
            if isinstance(v, (int, float)):
                num_value = float(v)
                # Exclude infinity and NaN values
                if math.isinf(num_value) or math.isnan(num_value):
                    continue
                total += num_value
                count += 1
            else:
                # Try to convert string numbers and other convertible types
                try:
                    num_value = float(v)
                    # Exclude infinity and NaN values
                    if math.isinf(num_value) or math.isnan(num_value):
                        continue
                    total += num_value
                    count += 1
                except (ValueError, TypeError):
                    # Skip values that can't be converted to float (e.g., complex, invalid strings)
                    continue

    if count == 0:
        return 0.0
    
    return total / count

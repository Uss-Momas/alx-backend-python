#!/usr/bin/env python3
"""
duck type annotations
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safe first element function
    Receives a sequence of Any type
    returns Any element type or NoneType
    """
    if lst:
        return lst[0]
    else:
        return None

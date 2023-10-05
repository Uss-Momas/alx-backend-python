#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    receives a multiplier
    and return a function
    """
    def f(value):
        return value * multiplier
    return f

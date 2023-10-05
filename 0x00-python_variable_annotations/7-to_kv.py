#!/usr/bin/env python3
"""
to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that receives multiple types in args
    returns a tupe of string and float
    """
    return (k, v ** 2)

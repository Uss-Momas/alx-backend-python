#!/usr/bin/env python3
"""Async comprehension module"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    results = [_ async for _ in async_generator()]
    return results

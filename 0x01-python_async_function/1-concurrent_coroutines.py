#!/usr/bin/env python3
"""module with multiple concurrent coroutines"""
from typing import List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine function that executes another coroutine"""
    future_values = []
    for _ in range(0, n):
        future_values.append(wait_random(max_delay))
    future_values = asyncio.as_completed(future_values)
    delays_values = [await future for future in future_values]
    return delays_values

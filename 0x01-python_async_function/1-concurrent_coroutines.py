#!/usr/bin/env python3
"""module with multiple concurrent coroutines"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine function that executes another coroutine"""
    delays_list = []
    for i in range(0, n):
        value = await wait_random(max_delay)
        delays_list.append(value)
    return delays_list

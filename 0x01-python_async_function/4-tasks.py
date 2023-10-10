#!/usr/bin/env python3
"""
4-tasks module
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine function that executes another coroutine"""
    future_values = []
    for _ in range(n):
        future_values.append(task_wait_random(max_delay))
    future_values = asyncio.as_completed(future_values)
    delays_list = []
    for future in future_values:
        value = await future
        delays_list.append(value)
    return delays_list

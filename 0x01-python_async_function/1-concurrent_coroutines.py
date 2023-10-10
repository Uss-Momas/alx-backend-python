#!/usr/bin/env python3
"""module with multiple concurrent coroutines"""
from typing import Any, List
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine function that executes another coroutine"""
    future_values = []
    for _ in range(0, n):
        future_values.append(wait_random(max_delay))
    # quick_sort(delays_list, 0, len(delays_list) - 1)
    future_values = asyncio.as_completed(future_values)
    delays_values = [await future for future in future_values]
    return delays_values


def quick_sort(target_list, low: Any, high: Any) -> None:
    """using the quicksort algorithm to sort a list"""
    if low < high:
        pi = partition(target_list, low, high)
        quick_sort(target_list, low, pi - 1)
        quick_sort(target_list, pi + 1, high)


def partition(array, low, high):
    """find partition position"""
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

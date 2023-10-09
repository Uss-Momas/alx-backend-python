#!/usr/bin/env python3
"""
4-tasks module
"""
from typing import Any, List


wait_random = __import__("0-basic_async_syntax").wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine function that executes another coroutine"""
    delays_list = []
    for i in range(0, n):
        value = await task_wait_random(max_delay)
        delays_list.append(value)
    quick_sort(delays_list, 0, len(delays_list) - 1)
    return delays_list


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

#!/usr/bin/env python3
"""Async generator module"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator  of 10 numbers"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

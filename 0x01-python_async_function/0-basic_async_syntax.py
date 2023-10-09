#!/usr/bin/env python3
"""module using basyc async syntax"""
import asyncio
import random


async def wait_random(max_delay=10):
    """function that receives a integer argument used to generate
    a random number
    returns the generated random number after sleeping
    """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n

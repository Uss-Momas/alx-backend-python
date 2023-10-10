#!/usr/bin/env python3
"""Async comprehension module"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """async comprehension"""
    results = [i async for i in async_generator()]
    return results

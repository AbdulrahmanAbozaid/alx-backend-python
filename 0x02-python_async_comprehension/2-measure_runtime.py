#!/usr/bin/env python3
"""
coroutine will collect 10
"""
from typing import Coroutine
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronously generates random float numbers between 0 and 10.
    The coroutine loops 10 times
    """
    ct = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - ct

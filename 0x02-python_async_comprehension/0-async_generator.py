#!/usr/bin/env python3
"""
0. Async Generator
"""
import random
from collections.abc import AsyncGenerator 
import asyncio


async def async_generator() -> AsyncGenerator[float]:
    """
    coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

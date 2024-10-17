#!/usr/bin/env python3
"""
Asynchronously generates random float numbers
"""
import asyncio
import random
from collections.abc import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates random float numbers between 0 and 10.
    The coroutine loops 10 times, each time asynchronously waiting
    1 second before yielding a random number.
    """
    for _ in range(10):  # Loop exactly 10 times
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

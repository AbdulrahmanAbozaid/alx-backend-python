#!/usr/bin/env python3
"""
coroutine will collect 10
"""
from typing import AsyncIterator, Coroutine, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Coroutine[None, None, List[float]]:
    """
    Asynchronously generates random float numbers between 0 and 10.
    The coroutine loops 10 times
    """
    return [i async for i in async_generator()]

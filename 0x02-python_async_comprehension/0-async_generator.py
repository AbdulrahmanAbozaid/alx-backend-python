#!/usr/bin/env python3
"""
0. Async Generator
"""
import random
from collections.abc import AsyncGenerator, Coroutine, Generator
import asyncio


async def async_generator() -> AsyncGenerator[float]:
    for _ in range(10):
        yield await asyncio.sleep(1, result=random.uniform(0, 10))

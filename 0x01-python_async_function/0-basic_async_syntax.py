#!/usr/bin/env python3
"""
Module for basic asynchronous syntax.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (inclusive) seconds.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

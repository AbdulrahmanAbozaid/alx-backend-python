#!/usr/bin/env python3
"""
Module for working with asyncio Tasks.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Return an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay.

    Returns:
        asyncio.Task: The created asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))

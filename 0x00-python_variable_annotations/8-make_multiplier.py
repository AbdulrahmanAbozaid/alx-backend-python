#!/usr/bin/env python3
"""
Module for task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier and
    returns a function that multiplies by that multiplier.
    """
    return lambda x: x * multiplier

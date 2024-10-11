#!/usr/bin/env python3
"""
Module for task 9
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list of sequences and returns a list of tuples.
    Each tuple contains the sequence and its length.
    """
    return [(i, len(i)) for i in lst]

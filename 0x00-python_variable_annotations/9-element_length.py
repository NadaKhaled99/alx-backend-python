#!/usr/bin/env python3
"""Function element_length"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples of sequence and int"""
    return [(i, len(i)) for i in lst]

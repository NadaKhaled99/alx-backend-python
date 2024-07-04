#!/usr/bin/env python3
"""Function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies the float"""
    return lambda x: x * multiplier

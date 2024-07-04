#!/usr/bin/env python3
"""Function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns the sum as float"""
    a: float = 0.0
    for i in input_list:
        a += i
    return a

#!/usr/bin/env python3
"""Define duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Type of elements of input are not known"""
    if lst:
        return lst[0]
    else:
        return None

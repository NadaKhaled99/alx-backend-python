#!/usr/bin/env python3
'''Async comprehension.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Create list of 10 num generator
    '''
    return [num async for num in async_generator()]

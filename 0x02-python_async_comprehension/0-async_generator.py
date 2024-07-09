#!/usr/bin/env python3
'''Async comprehension.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generate sequence of 10 num.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

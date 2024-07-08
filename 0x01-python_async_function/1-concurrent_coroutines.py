#!/usr/bin/env python3
"""Execute multiple coroutines"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of the delays."""
    future = [wait_random(max_delay) for _ in range(n)]
    future = asyncio.as_completed(future)
    delays = [await future for future in future]
    return delays

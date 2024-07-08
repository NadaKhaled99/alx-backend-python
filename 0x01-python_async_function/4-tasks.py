#!/usr/bin/env python3
"""Execute multiple coroutines"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delays."""
    future = [task_wait_random(max_delay) for _ in range(n)]
    future = asyncio.as_completed(future)
    delay = [await future for future in future]
    return delay

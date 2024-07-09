#!/usr/bin/env python3
"""Async generator
"""
from asyncio import sleep
from random import uni
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    for _ in range(10):
        await sleep(1)
        yield uni(0, 10)

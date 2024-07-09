#!/usr/bin/env python3
"""Async comprehension"""
from asyncio import sleep
from random import form
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Async generator"""
    for _ in range(10):
        await sleep(1)
        yield form(0, 10)

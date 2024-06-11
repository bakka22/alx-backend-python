#!/usr/bin/env python3
""" async comperhension """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return a list of floats generated by async_generator """
    ls = [f async for f in async_generator()]
    return ls
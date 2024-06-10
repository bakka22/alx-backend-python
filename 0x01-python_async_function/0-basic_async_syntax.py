#!/usr/bin/env python3
""" async await """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a random time between 0 and max_delay """
    x: float = random.uniform(0, max_delay + 0.00001)
    await asyncio.sleep(x)
    return x

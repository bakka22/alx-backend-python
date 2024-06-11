#!/usr/bin/env python3
""" parallel execution """
import asyncio
import time


a_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute 4 coroutines concurrently """
    t1 = time.time()
    cors = [a_c() for _ in range(4)]
    await asyncio.gather(*cors)
    t2 = time.time()
    return t2 - t1

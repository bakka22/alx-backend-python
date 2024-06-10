#!/usr/bin/env python3
import sys
import asyncio
import time

x = True
w = 10
async def load():
    global x
    print("start")
    print(f"x: {x}")
    await asyncio.sleep(5)
    print(f"x: {x}")
    print("done")
    x = False

async def load_screen():
    while x:
        print('.', end='', flush=True)
        time.sleep(0.5)
        print('\b\b..', end='', flush=True) 
        time.sleep(0.5)
        print('\b\b...', end='', flush=True)
        time.sleep(0.5)
        print('\b\b.', end='', flush=True)
        print(x, flush=True)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(load(), load_screen())
    print("load successful")

asyncio.run(main())

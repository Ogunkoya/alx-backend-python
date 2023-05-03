#!/usr/bin/env python3

import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime():
    start_time = asyncio.get_running_loop().time()  # Get the current event loop's time
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = asyncio.get_running_loop().time()  # Get the current event loop's time
    return end_time - start_time
#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield 10*random.random()  # Yield a random number between 0 and 10

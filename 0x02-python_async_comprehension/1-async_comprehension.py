#!/usr/bin/env python3

import asyncio
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    # Collect 10 random numbers using an async comprehension over async_generator
    random_numbers = [num async for num in async_generator()]
    return random_numbers
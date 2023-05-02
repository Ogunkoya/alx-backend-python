#!/usr/bin/env python3

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for i in range(n):
        task = task_wait_random(max_delay)
        await task
        delay = task.result()
        delays.append(delay)
    return delays
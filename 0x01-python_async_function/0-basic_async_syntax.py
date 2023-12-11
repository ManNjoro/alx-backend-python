#!/usr/bin/env python3
'''
Simple script with an asynchronous function 'wait_random'
to wait for a random number of seconds.
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time

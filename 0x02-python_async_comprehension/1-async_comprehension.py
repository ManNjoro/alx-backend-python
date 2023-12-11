#!/usr/bin/env python3
'''
A script that creates a list of 10 numbers from an async generator.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a async generator.
    '''
    return [num async for num in async_generator()]

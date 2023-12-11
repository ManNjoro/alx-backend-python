#!/usr/bin/env python3
'''
Simple script to measure the average runtime
of the 'wait_n' asynchronous function.
'''

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(num_executions: int, max_delay: int) -> float:
    '''
    Computes the average runtime of the 'wait_n' asynchronous function.
    '''
    start_time = time.time()
    asyncio.run(wait_n(num_executions, max_delay))
    return (time.time() - start_time) / num_executions

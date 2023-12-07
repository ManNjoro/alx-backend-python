#!/usr/bin/env python3
'''
Simple script to create a multiplier function.
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function.

    Parameters:
    - multiplier (float): The constant multiplier.

    Returns:
    - Callable: A function that takes a float as input and returns
                the result of multiplying it by the specified multiplier.
    '''
    return lambda x: x * multiplier

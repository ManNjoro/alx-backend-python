#!/usr/bin/env python3
'''
Simple script with a 'to_kv' function to create a key-value pair
where the key is a string and the value is the square of an integer or float.
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Returns:
    - Tuple[str, float]: A tuple representing the key-value pair,
                        where the key is a string, and the value is the square
                        of the input (converted to float).
    '''
    return (k, float(v**2))

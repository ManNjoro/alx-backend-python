#!/usr/bin/env python3
'''
Simple script to calculate the length of each element in an iterable.
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Calculate the length of each element in the given iterable.
    '''
    return [(i, len(i)) for i in lst]

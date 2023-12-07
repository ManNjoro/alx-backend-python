#!/usr/bin/env python3
'''
Simple script with a 'sum_mixed_list' function to calculate
the sum of a list of mixed types (int or float).
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Calculate the sum of a list containing a mixture of integers and floats.

    Parameters:
    - mxd_lst: The input list containing integers and/or floats.

    Returns:
    - float: The sum of the input list after converting all elements to floats
    '''
    return float(sum(mxd_lst))

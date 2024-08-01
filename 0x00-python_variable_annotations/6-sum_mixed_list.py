#!/usr/bin/env python3
""" type annotations """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return the sum of all of the list elements """
    return sum(mxd_lst)

#!/usr/bin/env python3
""" type annotations """
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """ return the sum of all of the list elements """
    return sum(mxd_lst)

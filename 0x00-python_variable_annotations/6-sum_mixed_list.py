#!/usr/bin/python3
""" function arguments annotations """
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """ takes a list of floats and integers and return the sum
    of its values """
    return sum(mxd_lst)

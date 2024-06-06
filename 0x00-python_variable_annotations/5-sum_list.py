#!/usr/bin/env python3
""" function arguments annotations """
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ takes a list of floats and returns the sum of its values """
    return sum(input_list)

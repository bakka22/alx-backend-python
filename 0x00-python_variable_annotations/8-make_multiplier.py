#!/usr/bin/env python3
""" functions annotations """
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """ takes a float multiplier and returns a function that
    multiplies a flost by the multiplier """
    def multi(n: float) -> float:
        """ takes a float and multiply it by the multiplier """
        return n * multiplier
    return multi

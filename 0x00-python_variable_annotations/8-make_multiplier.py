#!/usr/bin/env python3
""" type annotations """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that multiplies a float by multiplier """
    return lambda x: x * multiplier

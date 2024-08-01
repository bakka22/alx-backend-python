#!/usr/bin/env python3
""" type annotations """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple containig a string and a float """
    return (k, v ** 2)

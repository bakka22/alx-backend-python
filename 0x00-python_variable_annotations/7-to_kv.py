#!/usr/bin/env python3
""" functions annotations """
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """ takes a string and a number and return a tuple containing both
    of them """
    return (k, v * v)

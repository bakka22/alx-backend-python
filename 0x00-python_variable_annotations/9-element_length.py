#!/usr/bin/env python3
""" type annotations """
from typing import Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]

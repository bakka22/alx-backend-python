#!/usr/bin/env python3
""" type annotations """
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list containig the sequence and its length """
    return [(i, len(i)) for i in lst]

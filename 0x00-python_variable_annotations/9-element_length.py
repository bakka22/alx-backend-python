#!/usr/bin/env python3
""" functions annotations """
import typing


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """ takes an iterable of sequences and return a list of tuples
    containing the sequence and its length """
    return [(i, len(i)) for i in lst]

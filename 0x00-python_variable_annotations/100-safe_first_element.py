#!/usr/bin/env python3
""" functions annotations """
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, None]:
    """ takes a sequence and return its first element """
    if lst:
        return lst[0]
    else:
        return None

#!/usr/bin/env python3
""" type annotations """
from typing import Mapping, Any, Union, TypeVar


x = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[x, None] = None) -> Union[Any, x]:
    """ safly get a value from a dict """
    if key in dct:
        return dct[key]
    else:
        return default

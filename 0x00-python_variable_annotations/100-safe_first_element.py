#!/usr/bin/env python3
""" type annotations """
from typing import Any, Union


def safe_first_element(lst: Union[Any, None]):
    """ safely return the first element of a list """
    if lst:
        return lst[0]
    else:
        return None

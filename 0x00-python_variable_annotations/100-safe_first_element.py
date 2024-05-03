#!/usr/bin/env python3
"""Defines duck typed function"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """The types of the elements of the input are not known"""
    if lst:
        return lst[0]
    else:
        return None

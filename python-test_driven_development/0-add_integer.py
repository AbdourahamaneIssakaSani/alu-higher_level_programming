#!/usr/bin/python3
"""Adds two numbers"""


def add_integer(a, b=98):
    """
    Returns sum of a and b
    - Args :
        a: int or float
        b: int or float, default 98
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b

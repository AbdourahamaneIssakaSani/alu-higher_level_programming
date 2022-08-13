#!/usr/bin/python3
"""Adds two numbers"""


def add_integer(a, b=98):
    """
    Returns sum of a and b
    - Args :
        a: int or float
        b: int or float, default 98
    """
    if type(a) != int or type(a) != float:
        raise(TypeError, "a must be an integer")
    if type(b) != int or type(b) != float:
        raise(TypeError, "b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

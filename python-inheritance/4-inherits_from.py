#!/usr/bin/python3
"""Checks object class"""


def inherits_from(obj, a_class):
    """Checks object class
    Args:
        - obj: object to class
        - a_class: class to check
    """
    return issubclass(obj, a_class)

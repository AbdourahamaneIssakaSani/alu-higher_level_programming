#!/usr/bin/python3
""""Doc"""


def print_square(size):
    """"Doc"""
    if size <= 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, (int,)):
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)

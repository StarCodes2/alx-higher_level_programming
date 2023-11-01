#!/usr/bin/python3
"""Defines a function that adds two numbers."""


def add_integer(a, b=98):
    """returns the result of the addition of two integers."""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b

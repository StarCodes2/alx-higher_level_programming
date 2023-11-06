#!/usr/bin/python3
"""define a function that returns a list of available attributes and methods
of an object."""


def lookup(obj):
    """returns a list of attributes and methods of an object."""
    return dir(obj)

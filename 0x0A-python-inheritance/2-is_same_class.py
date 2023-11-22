#!/usr/bin/python3
"""defines a function to check if an object is an instance of
a specific class."""


def is_same_class(obj, a_class):
    """Check if an object an instance of a given class."""
    if (type(obj) == a_class):
        return True
    else:
        return False

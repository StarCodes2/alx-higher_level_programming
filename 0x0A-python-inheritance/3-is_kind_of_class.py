#!/usr/bin/python3
"""defines a function to check if an object is an instance of
a specific class or a class derived from it."""


def is_kind_of_class(obj, a_class):
    """Check if an object an instance of a given class or a class derived
    from it."""
    if isinstance(obj, a_class):
        return True
    else:
        return False

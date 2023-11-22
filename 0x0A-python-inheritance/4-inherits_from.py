#!/usr/bin/python3
"""defines a function to check if an object is an instance of
a specific class or a class derived from it."""


def inherits_from(obj, a_class):
    """Check if an object an instance of a given class or a class derived
    from it."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

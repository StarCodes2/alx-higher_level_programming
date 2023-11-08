#!/usr/bin/python3
"""Defines a function that returns the dictionary description
for json serialization of an object."""


def class_to_json(obj):
    """returns the dictionary description for json serialization
    of an object."""
    return obj.__dict__

#!/usr/bin/python3
"""Defines a base class."""


class Base:
    """Defines one private class attribute and increments it everytime a new
    instance is created, and one public instance attribute which is
    assigned the value of class attribute if the if id is None."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the public instance attribute."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

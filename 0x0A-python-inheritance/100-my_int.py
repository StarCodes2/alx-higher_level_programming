#!/usr/bin/python3
"""Defines a class MyInt that inherit from int."""


class MyInt(int):
    """Overrides the __ne__() and __eq__() methods inherited from int,
    inverting the normal results."""

    def __eq__(self, value):
        """Returns false if the values are equal and true if they are not."""
        return self.real != value

    def __ne__(self, value):
        """Returns false if values are not equal and true if they are."""
        return self.real == value

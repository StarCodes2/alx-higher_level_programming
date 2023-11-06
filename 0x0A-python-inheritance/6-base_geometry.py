#!/usr/bin/python3
"""Defines a base class called BaseGeometry."""


class BaseGeometry:
    """raise an exception when the area method is called."""
    def area(self):
        """raise an exception."""
        raise Exception("area() is not implemented")

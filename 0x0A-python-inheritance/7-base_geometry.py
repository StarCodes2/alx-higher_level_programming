#!/usr/bin/python3
"""Defines a base class called BaseGeometry."""


class BaseGeometry:
    """raise an exception when the area method is called."""
    def area(self):
        """raise an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

        return value

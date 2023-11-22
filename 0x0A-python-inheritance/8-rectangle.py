#!/usr/bin/python3
"""Defines a base class called Rectangle that inherit BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """raise an exception when the area method is called."""
    def __init__(self, width, height):
        """initialises the instance attributes."""
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

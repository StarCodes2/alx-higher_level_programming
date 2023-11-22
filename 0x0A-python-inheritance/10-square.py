#!/usr/bin/python3
"""Defines a base class called Square that inherit Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initialises the instance attributes."""
    def __init__(self, size):
        """initialises the instance attributes."""
        self.__size = self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

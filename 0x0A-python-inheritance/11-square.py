#!/usr/bin/python3
"""Defines a base class called Square that inherit Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initialises the instance attributes."""
    def __init__(self, size):
        """initialises the instance attributes."""
        self.__size = self.integer_validator('size', size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Computes an returns the area of a square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Returns a string description of the square."""
        return ("[Square] {}/{}".format(self.__size, self.__size))

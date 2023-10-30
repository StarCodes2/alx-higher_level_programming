#!/usr/bin/python3
"""defines class called Rectangle."""


class Rectangle:
    """Class defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Intialized with optional width and height."""
        self.width = width
        self.height = height

    @property
    def height(self):
        """returns the value of the private attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the private attribute height."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """return the value of the attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the private attribute width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

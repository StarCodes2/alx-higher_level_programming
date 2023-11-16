#!/usr/bin/python3
"""Defines a class that inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """Defines the properties of a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the instance attributes and base class public
        attribute."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of value."""
        return self.__width

    @width.setter
    def width(self, width):
        """Assigns a value to width."""
        self.__width = width

    @property
    def height(self):
        """Returns the value of height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Assigns a value to height."""
        self.__height = height

    @property
    def x(self):
        """Returns the value of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Assigns a value to x."""
        self.__x = x

    @property
    def y(self):
        """Returns the value of y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Assigns a value to y."""
        self.__y = y

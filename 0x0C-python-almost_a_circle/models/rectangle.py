#!/usr/bin/python3
"""Defines a class that inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """Defines the properties of a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the instance attributes and base class public
        attribute."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of value."""
        return self.__width

    @width.setter
    def width(self, width):
        """Assigns a value to width."""
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Returns the value of height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Assigns a value to height."""
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Returns the value of x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Assigns a value to x."""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Returns the value of y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Assigns a value to y."""
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """Returns the area of a rectangle."""
        return (self.width * self.height)

    def display(self):
        """Prints a rectangle in stdout."""
        for y in range(self.y):
            print()

        for i in range(self.height):
            for x in range(self.x):
                print(end=" ")

            for j in range(self.width):
                print("#", end="")

            print()

    def __str__(self):
        """Returns a string with the instance class and attributes values."""
        line = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
        return line

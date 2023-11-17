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

    def update(self, *args, **kwarg):
        """Assigns an argument to each attribute."""
        if (args and len(args) != 0):
            i = 0
            for arg in args:
                if (i == 0):
                    if (arg is None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif (i == 1):
                    self.width = arg
                elif (i == 2):
                    self.height = arg
                elif (i == 3):
                    self.x = arg
                elif (i == 4):
                    self.y = arg
                a += 1

        elif (kwarg and len(kwarg) != 0):
            for key, arg in kwarg.items():
                if (key == 'id'):
                    if (arg is None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif (key == 'width'):
                    self.width = arg
                elif (key == 'height'):
                    self.height = arg
                elif (key == 'x'):
                    self.x = arg
                elif (key == 'y'):
                    self.y = arg

    def to_dictionary(self):
        """Returns a dictionary representation of an instance of Rectangle."""
        d_rep = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

        return d_rep

    def __str__(self):
        """Returns a string with the instance class and attributes values."""
        line = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
        return line

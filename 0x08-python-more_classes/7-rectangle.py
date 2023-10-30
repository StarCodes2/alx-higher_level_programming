#!/usr/bin/python3
"""defines class called Rectangle."""


class Rectangle:
    """Class defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intialized with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Returns a printable string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += str(self.print_symbol)
            if i != self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        rec = "Rectangle(" + str(self.__width) + ", "
        rec += str(self.__height) + ")"
        return rec

    def __del__(self):
        """Prints a message everytime an instance of rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

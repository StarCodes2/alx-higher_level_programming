#!/usr/bin/python3
"""Defines the Square class that inherits from the Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines and initialise instance attributes, override the update()
    method."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialises the instance attributes."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size a side of the square."""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the value of the attributes  width and height."""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Overrides the update method inherited from Rectangle, used to
        update the attributes inherited from Rectangle."""
        if (args and len(args) != 0):
            i = 0
            for arg in args:
                if (i == 0):
                    if (arg is None):
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif (i == 1):
                    self.size = arg
                elif (i == 2):
                    self.x = arg
                elif (i == 3):
                    self.y = arg
                i += 1

        elif (kwargs and len(kwargs)):
            for key, arg in kwargs.items():
                if (key == 'id'):
                    if (arg is None):
                        self.__init__(self.size, self.x, self.y, self.id)
                    else:
                        self.id = arg
                elif (key == 'size'):
                    self.size = arg
                elif (key == 'x'):
                    self.x = arg
                elif (key == 'y'):
                    self.y = arg

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        s_rep = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

        return s_rep

    def __str__(self):
        """Overloads the __str__() method inherited from Rectangle."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

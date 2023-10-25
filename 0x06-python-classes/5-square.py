#!/usr/bin/python3
"""Define class square"""


class Square:
    """a class with an init size attribute."""
    def __init__(self, size=0):
        """Initializes the size attribute
        and defines a public instance method: def area(self):
        that returns the current square area."""
        self.__size = size

    @property
    def size(self):
        """returns the value of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """modifies the value of size."""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """returns the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """prints a square with # characters."""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()

        print()

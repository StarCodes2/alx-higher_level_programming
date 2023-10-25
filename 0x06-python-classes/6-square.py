#!/usr/bin/python3
"""Define class square"""


class Square:
    """a class with an init size attribute."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size and position attributes
        and defines a public instance method: def area(self):
        that returns the current square area."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """return the content of ppsition."""
        return self.__position

    @position.setter
    def position(self, position):
        """modifies the content of position."""
        if (isinstance(position, tuple) and
                len(position) == 2 and
                all(isinstance(num, int) for num in position) and
                all(num >= 0 for num in position)):
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """returns the area of a square."""
        return self.__size * self.__size

    def my_print(self):
        """prints a square with # characters."""
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            [print(" ", end="") for k in range(self.__position[0])]
            for j in range(self.__size):
                print('#', end="")
            print()

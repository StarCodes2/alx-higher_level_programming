#!/usr/bin/python3
"""Define class square"""


class Square:
    """a class with an init size attribute."""
    def __init__(self, size=0):
        """Initializes the size attribute."""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

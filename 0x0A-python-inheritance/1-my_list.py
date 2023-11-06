#!/usr/bin/python3
"""Defines a class that inherits from list."""


class MyList(list):
    """defines a method that prints a sorted list."""
    def print_sorted(self):
        """prints a sorted list."""
        print(sorted(self))

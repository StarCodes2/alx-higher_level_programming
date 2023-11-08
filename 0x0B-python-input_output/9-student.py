#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """Defines 3 public instance attributes a function to initialise them
    and a method that retrieves the dictionary representation of an
    instance of Student."""
    def __init__(self, first_name, last_name, age):
        """Initialises the instance attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of instance of Student."""
        return self.__dict__

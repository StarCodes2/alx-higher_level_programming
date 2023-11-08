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

    def to_json(self, attrs=None):
        """Returns the dictionary representation of instance of Student."""
        if type(attrs) == list and all(type(x) == str for x in attrs):
            return {x: self.__dict__[x] for x in self.__dict__
                    if x in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of Student with the content of the
        dictionary json."""
        for i, j in json.items():
            setattr(self, i, j)

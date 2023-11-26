#!/usr/bin/python3
"""Defines a base class."""
import json


class Base:
    """Defines one private class attribute and increments it everytime a new
    instance is created, and one public instance attribute which is
    assigned the value of class attribute if the if id is None."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the public instance attribute."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a dictionary to a json string."""
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a list's json serialization to a file."""
        fn = cls.__name__ + ".json"
        with open(fn, "w") as jf:
            if (list_objs is None):
                jf.write("[]")
            else:
                ld = [a.to_dictionary() for a in list_objs]
                jf.write(Base.to_json_string(ld))

    @staticmethod
    def from_json_string(json_string):
        """Deserializes a json string and return it."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance from the class of the instance that called
        it and return the new instance."""
        if (dictionary) and (dictionary != {}):
            if (cls.__name__ == "Square"):
                new_ins = cls(1)
            elif (cls.__name__ == "Rectangle"):
                new_ins = cls(1, 1)
            new_ins.update(**dictionary)

            return new_ins

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances created from the content of a file."""
        fn = cls.__name__ + ".json"

        try:
            with open(fn, "r") as jfile:
                diction = Base.from_json_string(jfile.read())
                lists = [cls.create(**a) for a in diction]
                return lists
        except IOError:
            return []

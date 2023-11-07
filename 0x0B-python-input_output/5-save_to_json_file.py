#!/usr/bin/python3
"""Defines a function that write an object to file in json string
representation."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json representation."""
    with open(filename, mode="w", encoding="utf-8") as my_json:
        json.dump(my_obj, my_json)

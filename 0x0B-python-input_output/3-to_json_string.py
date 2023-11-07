#!/usr/bin/python3
"""Defines a that turns an object to json representation."""
import json


def to_json_string(my_obj):
    """Returns the json representation string of an object."""
    return json.dumps(my_obj)

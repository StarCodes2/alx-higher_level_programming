#!/usr/bin/python3
"""Defines a function that creates an object from a json file."""
import json


def load_from_json_file(filename):
    """Creates an object from the content of a json file."""
    with open(filename, encoding="utf-8") as jf:
        return json.load(jf)

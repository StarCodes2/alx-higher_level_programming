#!/usr/bin/python3
"""Defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file."""
    with open(filename, mode="w", encoding="utf-8") as myfile:
        return myfile.write(text)

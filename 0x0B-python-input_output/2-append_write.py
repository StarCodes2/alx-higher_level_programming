#!/usr/bin/python3
"""Defines a function that appends string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to the content of a text file and the file
    doesn't exist it is created."""
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)

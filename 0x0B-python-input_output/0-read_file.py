#!/usr/bin/python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())

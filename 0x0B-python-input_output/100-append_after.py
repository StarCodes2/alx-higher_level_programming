#!/usr/bin/python3
"""Defines a function to insert text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line contain a particlar text."""
    lines = ""
    with open(filename, encoding="utf-8") as fs:
        for line in fs:
            lines += line
            if search_string in line:
                lines += new_string

    with open(filename, mode="w", encoding="utf-8") as fs:
        fs.write(lines)

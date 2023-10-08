#!/usr/bin/python3
def no_c(my_string):
    """Remove the characters C and c from a list and return the new list"""
    new_string = ""
    for value in my_string:
        if value != "c" and value != "C":
            new_string = new_string + value

    return new_string

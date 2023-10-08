#!/usr/bin/python3
def no_c(my_string):
    """Remove the characters C and c from a list and return the new list"""
    size = len(my_string)
    new_string = ""
    for idx in range(size):
        if my_string[idx] == "c" or my_string[idx] == "C":
            new_string = new_string + my_string[idx]

    return new_string

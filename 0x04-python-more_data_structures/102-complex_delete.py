#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary."""
    if a_dictionary is not None:
        while value in a_dictionary.values():
            for key, val in a_dictionary.items():
                if val == value:
                    del a_dictionary[key]
                    break

    return a_dictionary

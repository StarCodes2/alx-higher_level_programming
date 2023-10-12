#!/usr/bin/python3
def best_score(a_dictionary):
    """Find the key with the highest value in a dictionaty of integer values"""
    key, h_value = None, 0
    if a_dictionary != None:
        for i, value in a_dictionary.items():
            if value > h_value:
                h_value = value
                key = i

    return key

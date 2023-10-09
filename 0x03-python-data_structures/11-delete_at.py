#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the element at idx from a list and returns the list"""
    if idx >= 0 and (len(my_list) - 1) >= idx:
        del my_list[idx]

    return my_list

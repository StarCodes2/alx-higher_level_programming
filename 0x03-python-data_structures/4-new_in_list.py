#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element at an index without modifying the original list"""
    new_list = my_list.copy()
    if idx >= 0 and (len(new_list) - 1) >= idx:
        new_list[idx] = element

    return new_list

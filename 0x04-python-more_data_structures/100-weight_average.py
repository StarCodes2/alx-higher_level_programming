#!/usr/bin/python3
def weight_average(my_list=[]):
    """Compute the weighted average of all integer tuple in a list"""
    a, b = 0, 0
    for value in my_list:
        a += value[0] * value[1]
        b += value[1]

    return a / b

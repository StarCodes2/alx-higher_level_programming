#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    i = size - 1
    while (i >= 0):
        print("{:d}".format(my_list[i]))
        i -= 1

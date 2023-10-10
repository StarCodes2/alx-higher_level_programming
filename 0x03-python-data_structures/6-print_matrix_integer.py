#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers"""
    for lists in matrix:
        size = (len(lists) - 1)
        for num in lists:
            print("{:d}".format(num), end="")
            if size > 0:
                print(end=" ")
                size -= 1

        print("")

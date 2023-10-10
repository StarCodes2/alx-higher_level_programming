#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add the values of two tuples"""
    a, b = (), ()
    size_a = len(tuple_a)
    size_b = len(tuple_b)

    if size_a == 0:
        a = (0, 0)
    elif size_a == 1:
        a = (tuple_a[0], 0)
    else:
        a = tuple_a

    if size_b == 0:
        b = (0, 0)
    elif size_b == 1:
        b = (tuple_b[0], 0)
    else:
        b = tuple_b

    return (a[0] + b[0], a[1] + b[1])

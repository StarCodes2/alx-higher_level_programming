#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()."""
    prt = True
    try:
        print('{:d}'.format(value))
    except (TypeError, ValueError):
        prt = False

    return prt

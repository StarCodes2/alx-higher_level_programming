#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    for i in range(x):
        try:
            print('{}'.format(my_list[i]), end="")

        except IndexError:
            print()
            return i

    print()
    return i + 1

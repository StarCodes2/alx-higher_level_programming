#!/usr/bin/python3
def remove_char_at(str, n):
    # creatsles a copg of a string removing the char at n, handles negative n
    result = ""
    size = len(str)

    if n >= size:
        result = str
    else:
        for index in range(size):
            if index != n and ((n + size) != index):
                result = result + str[index]

    return result

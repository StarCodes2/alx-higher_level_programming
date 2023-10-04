#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    size = len(str)

    if n >= size:
        result = str
    else:
        for index in range(size):
            if index != n:
                result = result + str[index]

    return result

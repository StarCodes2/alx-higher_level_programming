#!/usr/bin/python3
def uppercase(str):
    a, z, c = ord('a'), ord('z'), 0

    for index in range(len(str)):
        c = ord(str[index])
        if (c >= a) and (c <= z):
            c -= 32

        print("{:s}".format(chr(c)), end='')

    print()

#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    if (c % 2) != 0:
        c -= 32
    print("{:s}".format(chr(c)), end='')

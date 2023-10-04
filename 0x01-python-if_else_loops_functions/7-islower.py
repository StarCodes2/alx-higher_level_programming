#!/usr/bin/python3
def islower(c):
    a, z, s = ord('a'), ord('z'), ord(c)
    if (s >= a) and (s <= z):
        return True
    else:
        return False

#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    result = 0

    if size > 0:
        for value in argv[1:]:
            result += int(value)
        print("{:d}".format(result))
    else:
        print(0)

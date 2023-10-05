#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv) - 1
    if size > 0:
        if size == 1:
            print("{:d} argument:".format(size))
        else:
            print("{:d} arguments:".format(size))

        for index in range(1, size + 1):
            print("{:d}: {:s}".format(index, argv[index]))
    else:
        print("{:d} arguments.".format(size))

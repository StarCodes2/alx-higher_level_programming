#!/usr/bin/python3
for i in range(9):
    for n in range(i + 1, 10):
        print("{:d}{:d}".format(i, n), end='')

        if (i == 8) and (n == 9):
            continue

        print(", ", end='')

print()

#!/usr/bin/python3
""" To display the value of the X-Request-Id variable found in the header of a
response """
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    request = Request(argv[1])
    with urlopen(request) as response:
        header = response.headers
        print(header['X-Request-Id'])

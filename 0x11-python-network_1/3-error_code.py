#!/usr/bin/python3
""" sends a request to a given URL and displays the body of the response"""
from sys import argv
from urllib.request import Request, urlopen
import urllib.error


if __name__ == "__main__":
    request = Request(argv[1])
    try:
        with request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

#!/usr/bin/python3
""" Sends a request to the URL and displays the body of the response

Usage: ./7-error_code.py <url>
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code > 399:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

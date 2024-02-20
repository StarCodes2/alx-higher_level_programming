#!/usr/bin/python3
""" Sends a request to a given URL and displays the value of the variable
X-Request-Id in the response header

Usage: ./5-hbtn_header.py <URL>
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))

#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter, and
finally displays the body of the response

Usage: ./6-post_email.py <url> <email>
"""
import requests
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    r = requests.post(argv[1], data=value)
    print(r.text)

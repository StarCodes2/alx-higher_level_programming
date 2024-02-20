#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))

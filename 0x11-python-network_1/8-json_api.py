#!/usr/bin/python3
""" Takes in a letter and sends a POST request to the given URL with the letter
as a parameter.

Usage: ./8-json_api.py <letter>
"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    value = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status """
import requests


if __name__ == __main__:
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body reaponse:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

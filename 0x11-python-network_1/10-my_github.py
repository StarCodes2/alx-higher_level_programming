#!/usr/bin/python3
""" Takes your GitHub credentials (username and password) and uses the GitHu
API to display your id

Usage: ./10-my_github.py <username> <password or personal access token>
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=basic)
    print(r.json().get("id"))

#!/usr/bin/python3
""" Lists the last 10 commits to a given GitHub repository

Usage: ./100-github_commits.py <repo name> <repo owner>
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    res = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                res[i].get("sha"),
                res[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

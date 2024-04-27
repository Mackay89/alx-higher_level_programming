#!/usr/bin/python3
"""
Script that lists 10 most recent to oldest commts on give GitHub repository by the user.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])


    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"),commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

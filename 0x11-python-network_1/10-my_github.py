#!/usr/bin/python3
"""
Script that takes your Github credentials (username and password) and
uses the GitHub API to display your id.
"""
from sys import argv
import requests

if __name__ == "__main__":
    username = argv[1]
    token = argv[2]


    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(username, token))


    if resp.status_code == 200:
        user_data = resp.json()
        user_id = user_data.get("id")
        print(user_id)
    else:
        print(None)

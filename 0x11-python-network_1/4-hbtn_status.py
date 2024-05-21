#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    body = resp.text
    print("Body resp:")
    print("\t- type:{}".format(type(body)))
    print("\t- content: {}".format(body))

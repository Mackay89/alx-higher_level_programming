#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"


    resp = requests.get(url)
    body = resp.text


    print("Body resp:")
    print("\t- Type:", type(body))
    print("\t- Content:", body)

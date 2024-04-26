#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request


def fetch_status():
    """
    Fetch the status fromthe URL and prints response details
    """
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')


            print("Body response:")
            print("\t- type:", type(body))
            print("\t- content:", body)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    fetch_status()

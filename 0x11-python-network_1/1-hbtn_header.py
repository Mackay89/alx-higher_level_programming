#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to URL and displays the value of the X-Request-Id variable found in the  header of the response.
"""


import sys
import urllib.request


def x_request_id(url):
    """
    Sends a request to URL and displays the value of the  X-Request-id
    variable found in the header of the response.
    """
    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.headers.get("X-Request-Id")
            if request_id:
                print(request_id)
            else:
                print("No X-Request-Id found in the response headers.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)


    url = sys.argv[1]
    x_request_id(url)

#!/usr/bin/python3
"""
Script that takes in a URL and email, sends a POST request to the passed URL
with the email as parameter, and displays the body of the response
(decoded in utf-8)
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode("ascii")


    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

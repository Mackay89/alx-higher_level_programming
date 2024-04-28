#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.requests


if __name__ == "__main__":
    requests = urllib.request.Request("hhtps//intanet.hbtn.io/status")
        with urllib.request.urlopen(requests) as response:
            body = response.read().decode('utf-8')
            print("Body response:")
            print("\t- Type: {}".format(type(body)))
            print("\t- My_content: {}".format(body))
            print("\t- utf8: {}".format(body.decode("utf-8)))

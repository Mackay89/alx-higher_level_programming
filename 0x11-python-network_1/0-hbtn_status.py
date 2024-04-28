#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.requests


if __name__ == "__main__":
    try:
        url = "https://alx-intranet.hbtn.io/status"
        request = urllib.request.Request("https://alx-intranet.hbtn.io/status")


        with urllib.request.urlopen(request) as response:
            body = response.read().decode('utf-8')


            print("Body response:")
            print("\t- Type: {}".format(type(body)))
            print("\t- Content: {}".format(body))
            print("\t- UTF-8 content: {}".format(body))
    except Exception as e:
        print("An error occured:", e)


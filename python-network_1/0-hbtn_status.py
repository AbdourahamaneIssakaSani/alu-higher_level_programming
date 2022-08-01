#!/usr/bin/python3
"""I document you"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response.read()))
        print("\t- utf8 content: {}".format(response.read().decode("utf-8")))

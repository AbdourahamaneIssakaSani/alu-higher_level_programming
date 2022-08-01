#!/usr/bin/python3
"""Documented now"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    try:
        print("{}".format(response.headers["X-Request-Idd"]))
    except KeyError:
        print(None)

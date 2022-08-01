#!/usr/bin/python3
"""I documented you"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    """Documented"""
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Your email is: {}".format(content.decode("utf-8"))

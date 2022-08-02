#!/usr/bin/python3
"""Documented now"""
import requests
import requests.auth
import sys

if __name__ == '__main__':
    response = requests.get(
        url="https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(
            "AbdourahamaneIssakaSani",
            "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"
        )))
    try:
        json_response = response.json()
        print("{}".format(json_response["id"]))
    except:
        print(None)

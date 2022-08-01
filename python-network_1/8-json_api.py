#!/usr/bin/python3
"""Documented now"""
import requests
import sys

if __name__ == '__main__':
    params = sys.argv[1]
    response = requests.get("http://0.0.0.0:5000/search_user?q={}".format(params))
    try:
        json_response = response.json()
        if response.headers.get("Content-Type") == 'application/json':
            print("[{}] {}".format(json_response["id"], json_response["name"]))
        else:
            print("{}".format(response.text))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")

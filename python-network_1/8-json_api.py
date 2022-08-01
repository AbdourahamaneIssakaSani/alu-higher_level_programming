#!/usr/bin/python3
"""Documented now"""
import requests
import sys

if __name__ == '__main__':
    params = sys.argv[1] if len(sys.argv) == 1 else q = ""
    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": params})
    try:
        json_response = response.json()
        if response.headers.get("Content-Type") == 'application/json':
            print("[{}] {}".format(json_response["id"], json_response["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

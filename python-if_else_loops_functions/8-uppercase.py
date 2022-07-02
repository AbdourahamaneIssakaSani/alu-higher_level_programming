#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) < 97 or ord(char) > 122:
            char = chr(ord(char) - 32)
    return str

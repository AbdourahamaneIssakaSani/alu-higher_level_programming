#!/usr/bin/python3
""""Doc"""


def text_indentation(text):
    """"Doc"""
    if not isinstance(text, (str,)):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    for i in range(len(text)):
        if text[i] in characters:
            try:
                if text[i + 1] == " ":
                    text = text[:i + 1] + "\n\n" + text[i + 2:]
                else:
                    text = text[:i + 1] + "\n\n" + text[i + 1:]
            except IndexError:
                pass
    print(text, end="")

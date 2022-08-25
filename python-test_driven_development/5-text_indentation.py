#!/usr/bin/python3
""""Doc"""

def text_indentation(text):
    """ Doc here
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']

    idx = 0
    for char in text:
        if char in characters:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for char in text:
        if char in characters:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1

    print(text, end='')

# def text_indentation(text):
#     """"Doc"""
#     if not isinstance(text, (str,)):
#         raise TypeError("text must be a string")

#     characters = [".", "?", ":"]
#     for i in range(len(text)):
#         if text[i] in characters:
#             try:
#                 if text[i + 1] == " ":
#                     text = text[:i + 1] + "\n\n" + text[i + 2:]
#                 else:
#                     text = text[:i + 1] + "\n\n" + text[i + 1:]
#             except IndexError:
#                 pass
#     print(text, end="")

#!/usr/bin/python3
""""Doc"""


def text_indentation(text):
    """ Doc here
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")

# def text_indentation(text):
#     """"Doc"""
#     if not isinstance(text, (str,)):
#         raise TypeError("text must be a string")

#     characters = [".", "?", ":"]
#     index = 0
#     while index < len(text):
#         if text[index] in characters:
#             print(text[index], end="")
#             print('\n')
#             index += 1
#             if text[index] == " ":
#                 index += 1
#         else:
#             print(text[index], end="")
#             index += 1

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

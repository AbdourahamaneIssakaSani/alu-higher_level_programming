#!/usr/bin/python3
""""Peak"""


def find_peak(list_of_integers):
    """"Finds peak in recursive binary search"""
    if len(list_of_integers) % 2 == 0:
        mid = (len(list_of_integers) // 2) - 1
    else:
        len(list_of_integers) // 2

    if len(list_of_integers) <= 2:
        return
    elif len(list_of_integers) == 3 and list_of_integers[mid - 1] <= \
            list_of_integers[mid] and list_of_integers[mid] >= \
            list_of_integers[mid + 1]:
        return list_of_integers[mid]
    else:
        return find_peak(list_of_integers[:mid]) or \
               find_peak(list_of_integers[mid:])

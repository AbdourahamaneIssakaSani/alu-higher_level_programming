#!/usr/bin/python3
""""Peak"""


def find_peak(list_of_integers):
    """"Finds peak in recursive binary search"""
    if len(list_of_integers) % 2 == 0:
        mid = (len(list_of_integers) // 2) - 1
    else:
        mid = len(list_of_integers) // 2

    peak = list_of_integers[mid]

    if len(list_of_integers) <= 2:
        return max(list_of_integers)
    elif list_of_integers[mid - 1] <= \
            peak and peak >= \
            list_of_integers[mid + 1]:
        return peak
    else:
        return find_peak(list_of_integers[:mid]) and \
               find_peak(list_of_integers[mid:])

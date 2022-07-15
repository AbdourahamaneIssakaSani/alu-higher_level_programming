#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    for n in roman_string:
        if n in roman_numerals:
            sum_ += int(roman_numerals[n])
    return sum_

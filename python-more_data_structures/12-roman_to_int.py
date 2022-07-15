#!/usr/bin/python3
def roman_to_int(roman_string):
        if type(roman_string) != str or roman_string is None:
        return 0
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0
    sum_list = list()
    for i in range(len(roman_string)):
        try:
            if roman_string[i] == "I" and (roman_string[i + 1] == "V" or roman_string[i + 1] == "X"):
                sum_list.append(-int(roman_numerals[roman_string[i]]))
            else:
                sum_list.append(int(roman_numerals[roman_string[i]]))
        except IndexError:
            pass
    return sum(sum_list)

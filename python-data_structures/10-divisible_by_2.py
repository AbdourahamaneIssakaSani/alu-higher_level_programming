#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    n_list = list(my_list)
    for item in n_list:
        if item % 2 == 0:
            n_list[item] = True
        else:
            n_list[item] = False
    return n_list

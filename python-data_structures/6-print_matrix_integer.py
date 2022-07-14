#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for item in list_:
            print('{:d}'.format(item), end=" ")
        print()

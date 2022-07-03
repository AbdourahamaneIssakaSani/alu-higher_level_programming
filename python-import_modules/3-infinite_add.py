#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    args_number = len(argv) - 1

    if args_number > 0:
        if args_number == 1:
            print("{} argument:".format(args_number))
        else:
            print("{} arguments:".format(args_number))
        sum_ = 0
        for args in argv[1:]:
            sum_ += int(args)
        print("{}".format(sum_))
    else:
        print("{}".format(args_number))

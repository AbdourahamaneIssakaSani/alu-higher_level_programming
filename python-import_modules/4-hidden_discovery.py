#!/usr/bin/python3
if __name__ == '__main__':
    names = dir('hidden_4')
    names.sort()
    for attr in names:
        if attr[:2] != "__":
            print(attr)

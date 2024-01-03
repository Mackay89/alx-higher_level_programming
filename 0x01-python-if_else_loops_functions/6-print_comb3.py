#!/usr/bin/python3
for b in range(0, 9):
    for h in range(b + 1, 10):
        if b == 8:
            print("{}{}".format(b, h))
        else:
            print("{}{}".format(b, h), end=",")

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    if my_list is None:
        my_list = []

    for c in range(0, x):
        try:
            print("{:d}".format(my_list[c]), end='')
            count += 1
    except (TypeError, ValueError):
        continue

    print("")
    return (count)

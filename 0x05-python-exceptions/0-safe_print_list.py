#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    sum_count  = 0

    if my_list is None:
        my_list = []

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            sum_count = sum_count + 1
        except IndexError:
            continue

    print("")
    return (sum_count)

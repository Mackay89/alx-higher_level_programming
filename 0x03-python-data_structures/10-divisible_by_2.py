#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length_list = len(my_list)
    result_list = []
    for i in range(length_list):
        if my_list[i] % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)
    return result_list

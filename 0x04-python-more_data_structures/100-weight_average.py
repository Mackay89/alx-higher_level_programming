#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numer = 0
    den = 0
    for i in range(len(my_list):
        numer += my_list[i][0] * my_list[1][i]
        den += my_list[1][i]
    return (num / den)

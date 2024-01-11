#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avarage = sum(avar * weight for avar, weight in my_list)
    weight = sum(weight for _, weight in my_list)
    return avar / weight

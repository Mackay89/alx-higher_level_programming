#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul = {}
    for key in a_dictionary:
        mul[key] = a_dictionary[key] * 2
    return mul

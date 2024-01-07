#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_copy
    elif idx >= len(my_list):
        return my_copy
    new_copy = copy(my_list)
    new_copy[idx] = element
    return new_copy

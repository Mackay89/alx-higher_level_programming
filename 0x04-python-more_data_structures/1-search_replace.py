#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = mylist[:]
    for i in range(new_list):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for idx in range(len(my_list)):
        if new_list[idx] == search:
            new_list.append(replace)
        else:
            new_list.append(new_list[idx])
    return new_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if new == search else new for new in my_list]
    

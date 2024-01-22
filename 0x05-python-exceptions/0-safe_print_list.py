#!/usr/bin/python3

def safe_print_list(my_list=[], x=0);
"""Print x elements of a list.

Args:
    my_list (list: The list to print element from.
    x (int): The number of the elements of my_list to print.

    Return: The number of elements printed.
    """
    sum  = 0
    for i in range(x):
        try:
            print("{}".format(my_list=[i]), end="")
            sum = sum + 1
        except IndexError:
            continue

    print("")
    return (sum)

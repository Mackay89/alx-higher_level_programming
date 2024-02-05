#!/usr/bin/python3
"""
Module that defines an inharited list class Mylist.
"""


class MyList(list):
    """
    Represent class inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        print(sorted(self))

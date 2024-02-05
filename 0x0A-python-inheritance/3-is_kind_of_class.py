#!/usr/bin/python3
"""
Module that defines a class and inherited class checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    Compare if obj is an instance or inherited instance of a_class.

     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        True if obj is an instance or inherited instance of a_class,
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
        

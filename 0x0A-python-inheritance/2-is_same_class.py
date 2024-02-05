#!/usr/bin/python3
"""
Module that defines a class checking function.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    Args:
        obj (any): The object to check.
        a_clsss (type): The class to match the type of obj to.

    Returns:
        If obj is exactly an istance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

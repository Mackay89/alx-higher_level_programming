#!/usr/bin/python3
"""
Creat a  function that returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Represent a return list of an object's available attributes.
    """
    return (dir(obj))

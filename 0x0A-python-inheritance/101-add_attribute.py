#!/usr/bin/python3
"""
Module that defines a function that adds a new attribute to an object.
"""



def add_attribute(obj, attr, value):
    """ 
    Adds a new atrribute to an object if it's possible.

    Args:
        obj (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to obj.
        value (any): The  value of attr.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

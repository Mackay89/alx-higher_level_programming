#!/usr/bin/python3
"""
Module 0-add_integer.
Defines a function add_integer that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integer.


    Args:
        a (int or float): The first number.
        b (int or float): The second number.


    Returns:
        int: The sum of a and b.


    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if  not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float") 
    a = int(a)
    b = int(b)
    return a + b

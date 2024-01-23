#!/usr/bin/python3
"""Class Square that defines a square"""

class Square:
    """Define a square with private instance attribute:
    size and Instantiation with size (no type/value verification)"""

    def __init__(self, size):
        """Initialize class """
        self.__size = size

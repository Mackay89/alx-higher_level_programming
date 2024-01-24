#!/usr/bin/python3
"""Module for a square"""


class Square:
    """Define a square.

    This class represent a square and is used for storing the size of the square
    """
    
    def __init__(self, size):
        """
        Initialize the Square instance with given size.

        args:
            size (int: The size of the square.

        Return:
            None
        """
        self.__size = size

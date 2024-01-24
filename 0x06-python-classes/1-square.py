#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    Represent a square.

    This class represents a square and is used for storing the size of the square.
    """
    
    def __init__(self, size):
        """
        Initialize the Square instance with a given size.

        args:
            size (int): The size of the square.

        Returns:
            None
        """

        self.__size = size

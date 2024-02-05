#!/usr/bin/python3
"""
Module that defines a Rectangle subclass Square.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Represent the square.
    """

    def __init__(self. size):
        """
        Initialize a square.
    

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size


#!/usr/bin/python3
"""
Module that defines a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __iport__("7-base_geometry").BaseGeometry



class Rectangle(BaseGeometry):
    """
    Defines a rectangle using BaseGeometry.
    """


    def __init__(self, widt, height):
        """
        Intialize a Rectangle.


        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        self.integer-validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.height = height

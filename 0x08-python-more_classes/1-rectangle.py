#!/usr/bin/python3
"""
module that defines a class Rectangle.
"""


class Rectangle:
    """
    Represent a rectangle
    """


    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.


        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.width = width
        self.height = height


    @property
    def width(self):
        """
        Width retriver.


        Returns:
            int: The width of the rectangle.
        """

        return self.__width


    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.


        Args:
            value (int): Width of  the rectangle.


        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is les than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an intger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """
        Height retriver.


        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    
    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.


        Args:
            value (int): height of the rectangle.


        Raises:
            TypeError: if height is not an integer.
            VAalueError: if height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

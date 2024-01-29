#!/usr/bin/python3
"""
Module that defines a Rectangle class.
"""


class Rectangle:
    """
    Represent a rectangle.
    """


    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.


        Args:
            width (int): The width of the rectangle.
            height (int): the height of the rectangle.
        """

        self.wdth = width
        self.height = height


    @property
    def width(self):
        """
        Width retriver.


        Returns:
            int: The width of the rectangle.
        """
        
        return self.__width


    @property
    def height(self):
        """
        Height retriver.

        Returns:
            int: The height f the rectangle.
        """

        return self.__height

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.


        Args:
            value (int): The width to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.


        Args:
            value (int): The height to set.


        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """
        Calculate and return of the area of the rectangle.


        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.


        Returns:
            int: The perimeter of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

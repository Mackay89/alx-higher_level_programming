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
        Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self. width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeEror("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
         Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle

        Returns:
            int: The area of the rectangle.
        """
        return (self.width * self.height)


    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))


    def __str__(self):
        """
        Return the printable representation of the rectangle.

        Represents the rectangle with the # character.
        """
         if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height("\n")
            return ("".join(rect))

    def __repr__(self):
        """
        Return the string representation of the rectangle.
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """
        Print a massage for every deletion of a rectangle.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")


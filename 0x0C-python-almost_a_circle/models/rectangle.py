#!/usr/bin/python3
"""
Module that defines a rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represent a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """creates instance of rectangle.

        Args:
            width (int): The width of the  rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The coordinate of the  rectangle.
            id (int): The identity of the rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """
        Retrieve width.
        
        Returns:
            width (int): The width of the rectangle.
        """
        return self.__width


    @width.setter
    def width(self, value):
        """
        The property setter for width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            height(int): The height of the rectangle.
        """
        return self.__height


    @height.setter
    def height(self, value):
        """
        The property setter for height of the rectangle.

        Args:
            value (int): The height of rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """
        Retrieve x coordinate of the rectangle.

        Returns:
            int: x
        """
        return self.__x


    @x.setter
    def x(self, value):
        """
        The property setter for x.

        Args:
            x (int): The property setter for x.

        Raises:
            TypeError: If x is not integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @property
    def y(self):
        """
        Retrieve y coordinate of the rectangle.

        Returns:
            int: y
        """
        return self.__y


    @y.setter
    def y(self, value):
        """
        The property setter for y.

        Args:
            value (int): The property of y.

        Raises:
            TypeError: If y is not an integer.
            ValueError: If y is less than or equal to zero.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """
        Calculates the area of a Rectangle.
        """
        return self.__width * self.__height


    def display(self):
        """
        Print the rectangle using the '#' character.
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print('#', end"") for w in range(self.__width)]
            print("")


    def update(self, *args, **kwargs):
        """
        Update the rectangle.

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """

        # print("args {}".format(type(args)))
        # print("kwargs {}".format(type(kwargs)))
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: rectangle.
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)


    def __str__(self):
        """
        return the print() and str() representation of the rectangle.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.__id, self.__x, self.__y,
                self.__width, self.__height)



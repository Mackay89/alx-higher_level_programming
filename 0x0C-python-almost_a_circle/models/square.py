#!/usr/bin/python3
"""
Module that defines a class Square.
"""
from insect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represent class that defines properties of Square.
    """


    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square.

        Args:
            size (int): The size of the Square.
            x (int): The x coordinate of the Square.
            y (int): The y coordinate of the Square.
            id (int): The identity of the Square.
        """
        super().__init__(size, size, x, y, id)
        self.__size = size


    @property
    def size(self):
        """
        Get the size of the Square.
        """
        return self.__width


    @size.setter
    def size(self, value):
        """
        Setter size
        """
        self.__width = value
        self.__height = value


    def __str__(self) -> str:
        """
        Represent the string.
        """
        id = self.__id
        size = self.__size
        x = self.__x
        y = self.__y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)


    def update(self, *args, **kwargs):
        """
        Update the arguments.

        Args:
            *args (int): The new attribute values.
            id (int): The argument represents id attribute.
            size (int): The argument represent size attribute.
            x (int): The argument represent x attribute.
            y (int): The argument represent y attribute.
            **kwargs (dict): The new key/value pairs of attributes.
        """
        attr = ['id', 'size', 'x', 'y']
        if args:
            for a, num in zip(attr, args):
                setattr(self, a, num)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)


    def to_dictionary(self) -> dict:
        """
        Represent the square to dictionary.
        """
        id = self.__id
        size = self.__size
        x = self.__x
        y = self.__y
        return {'id': id, 'x': x, 'size': size, 'y': y}

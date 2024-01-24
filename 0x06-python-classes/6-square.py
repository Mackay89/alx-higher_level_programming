#!/usr/bin/python3
"""
Creates class Square.

This module contains the Square class that represent a square
with a specified size and position.
"""


class Square:
    """
    Represents a square.


    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes a new Square instance.
        size (property): Getter and setter for size.
        position (property): Getter and setter for position.
        area(self): Calculate the area of the square.
        my_print(self): Print the square with the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        
        Raises:
            TypeError: If size is not an integer or if position is not a tuple
            of 2 positive integer.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size.

        Args:
            value (int): The size of the square.


        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def posision(self):
        """
        Getter for position.

        Returns:
            tuple: The position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integer.
        """

        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """ 
        Calculate the area of the square.


        Return:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square with the character '#'.

        If size is equal to to 0, print an empty line.
        Use position to add spaces.
        """

        if self.size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)



#!/usr/bin/python3
"""A module Square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif:
            self.__size = value

    @property
    def posision(self):
        """Getter method for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """ get area
        Return:
            area (int)
        """
        return self.__size ** 2

    def my_print(self):
        """
        print a square
        Return:
            None
        """
        if self.size == 0:
            print("")
        else:
            print("\n"*self.__position[1]; end="")
            for i in range(self._size):
                print(" "*self.__position[0], end="")
                print('#'*self.__size)

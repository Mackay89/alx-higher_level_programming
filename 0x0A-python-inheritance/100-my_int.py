#!/usr/bin/python3
"""
Module that defines a class MyInt that inherits from int.
"""



class MyInt(int):
    """
    Invert int operators == and !=.
    """

    def __eq__(self, value):
        """
        Override == operator with != behavior.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with == behavior.
        """
        return self.real == value

    def __str__(self):
        """
        Override __str__ method to display the value correctly.
        """
        return str(self.real)

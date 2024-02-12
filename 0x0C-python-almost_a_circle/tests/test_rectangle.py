#!/usr/bin/python3
"""
Defines unittest for models/ Rectangle.py base
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Define a unit for Rectangle model.
    """

    def test_initialization(self):
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.id, Rectangle._Base_nb_objects)
        r2 = Ractangle(1, 2)
        self. assertEqual(r2.id, Rectangle._Base_nb_objects)


if __name__ == '__main__':
    unittest.main()

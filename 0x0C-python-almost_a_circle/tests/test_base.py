#!/usr/bin/python3
"""
Defines unittests for base
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Represent the unit test for Base model.
    """


    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(Base1.id, 1)
        self.assertEqual(base2.id, 2)


    def test_saving_id(self):
        base = Base(100)
        self.assertEqual(Base.id, 100)


    def test_to_json_string_valid(self):
        pass


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
defines unittest for base.
"""


class TestSquare(unittest.TestCase):
    """
    Define unit test for a Square model.
    """


    def test_initialization_success(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s2.id, 6)


    def test_initialiization_without_arguments(self):


        self.assertRaises(TypeError, Square)


if __name__ == '__main__':
    unittest.main()

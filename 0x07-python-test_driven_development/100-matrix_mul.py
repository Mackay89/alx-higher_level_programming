#!/usr/bin/python3
"""
Module that defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """
    This module contain a function that multiplies of two matrices.

    Args:
        m_a (list of lists of int/float): Matrix to be multiplied.
        m_b (list of lists of int/float): Matrix to be multiplied.

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied
    Returns:
        A new list which is the outcome of the multiplication
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a lists")


    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be a lists")
    

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_b can't be empty")


    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")


    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")


    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")


    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        matrix1.append(my_row)

    matrix2 = []
    for row in m_a:
        my_row = []
        for colum in matrix1:
            product = 0
            for m in range(len(matrix1[0])):
                product += row[m] * colum[m]
            my_row.append(product)
        matrix2.append(my_row)

    return matrix2

 #!usr/bin/python3
"""
Define a matrix function that divides all alements of a matrix.
"""

def matrix_divided(matric, div):
    """
    Divide all elements of a matrix.

    Args:
        matrx (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.
    Returns:
        list of lists: The resulting matrix with elements rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integer or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrx):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element/div, 2) for element in row] for row in matrix]



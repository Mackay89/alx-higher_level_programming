#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for row in matrix:
        square.append([i**2 for i in row])
    return square

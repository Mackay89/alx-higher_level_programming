#!/usr/bin/python3
"""
Module that containing the function that read_file
"""


def read_file(filename=''):
    """
    Print the contents of a UTF8 text file to stdout.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')

#!/usr/bin/python3
"""
Module that defines a file-appending function.
"""


def append_write(filename="", text=""):
    """
    Represent appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)

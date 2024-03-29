#!/usr/bin/python3
"""
Module that defines a text-indentation function.
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args: 
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    a = 0
    while a < len(text):
        if text[a] == ' ' and (a == 0 or text[a - 1] in ".?:"):
            a += 1
            continue

        print(text[a], end="")

        if text[a] in ".?:":
            print("\n")
            a += 1
            while a < len(text) and text[a] == ' ':
                a += 1
            continue

        a += 1

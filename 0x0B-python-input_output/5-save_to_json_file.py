#!/usr/bin/python3
"""
Module that defines a JSON file-writing function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Represent write of an object to a text file using JSON.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

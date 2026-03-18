#!/usr/bin/python3
"""
This module contains a function that writes an object to a file
using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """
    # Open the file in write mode ('w') with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # json.dump (without 's') writes directly to the file object
        json.dump(my_obj, f)

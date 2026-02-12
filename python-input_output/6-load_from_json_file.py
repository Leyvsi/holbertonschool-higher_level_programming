#!/usr/bin/python3
"""
This module contains a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".
    """
    # Open the file in read mode ('r')
    with open(filename, "r", encoding="utf-8") as f:
        # json.load (without 's') reads directly from the file object
        return json.load(f)

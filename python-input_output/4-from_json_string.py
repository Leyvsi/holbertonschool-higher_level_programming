#!/usr/bin/python3
"""
This module contains a function that converts a JSON string to an object.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.
    """
    # json.loads converts a string (JSON format) into a Python object
    return json.loads(my_str)

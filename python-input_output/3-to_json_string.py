#!/usr/bin/python3
"""
This module contains a function that returns the JSON representation
of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    """
    # json.dumps converts a Python object into a JSON formatted string
    return json.dumps(my_obj)

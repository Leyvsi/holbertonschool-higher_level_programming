#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    """
    # Returns the __dict__ attribute of the object
    # This contains all the instance attributes in a dictionary format
    return obj.__dict__

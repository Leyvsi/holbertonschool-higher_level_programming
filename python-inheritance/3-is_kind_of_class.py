#!/usr/bin/python3
"""
This module contains a function that checks for class inheritance.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of, or inherited from, a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj matches the class or its ancestors, else False.
    """
    return isinstance(obj, a_class)

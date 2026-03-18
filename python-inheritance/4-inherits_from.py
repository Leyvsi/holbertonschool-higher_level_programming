#!/usr/bin/python3
"""
This module contains a function that checks for subclass inheritance.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is a subclass instance, but not the class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""
Module that provides a function to add two integers.

The function handles integers and floats, casts floats to integers,
and raises appropriate errors when inputs are invalid.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Raises a TypeError if a or b is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    A class with a public instance method area.
    """

    def area(self):
        """
        Method that raises an Exception because area is not implemented.
        """
        raise Exception("area() is not implemented")

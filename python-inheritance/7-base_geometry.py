#!/usr/bin/python3
"""
Module defining a class BaseGeometry with area and integer_validator.
"""


class BaseGeometry:
    """
    A class with methods for area and integer validation.
    """

    def area(self):
        """
        Method that raises an Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value as a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

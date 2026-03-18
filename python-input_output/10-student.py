#!/usr/bin/python3
"""
This module defines a Student class with attribute filtering.
"""


class Student:
    """
    Representation of a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first_name, last_name, and age.
        """
        # Public instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only those attributes are retrieved.
        """
        # If no filter is provided, return all attributes
        if attrs is None:
            return self.__dict__

        # If attrs is a list, filter the dictionary
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for key in attrs:
                # Check if the requested attribute exists in the instance
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        # Fallback if attrs is not a valid list of strings
        return self.__dict__

#!/usr/bin/python3
"""
This module defines a Student class with serialization and
deserialization capabilities.
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
        # If attrs is a list of strings, filter the attributes
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res

        # Otherwise, return all attributes
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.
        """
        # The json argument is a dictionary where keys are attribute names
        for key, value in json.items():
            # setattr() updates the attribute named 'key' with 'value'
            setattr(self, key, value)

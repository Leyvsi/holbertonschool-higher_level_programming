#!/usr/bin/python3
"""
This module defines a Student class.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        # Returns the dictionary of the instance attributes
        return self.__dict__

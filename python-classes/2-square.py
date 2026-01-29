#!/usr/bin/python3
"""This module defines a class Square with size validation."""


class Square:
    """Represents a square with private size and validation."""

    def __init__(self, size=0):
        """Initialize a square with size.

        Args:
            size (int): size of the square (default 0)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): new size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

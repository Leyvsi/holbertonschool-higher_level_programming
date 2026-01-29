#!/usr/bin/python3
"""This module defines a class Square with getter and setter for size and area."""


class Square:
    """Represents a square with size validation and area calculation."""

    def __init__(self, size=0):
        """Initialize a square with optional size.

        Args:
            size (int): size of the square (default 0)
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

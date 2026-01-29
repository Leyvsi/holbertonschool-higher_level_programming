#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""

class Square:
"""Represents a square with a private size."""
 
   def __init__(self, size):
"""Initialize a square with size.

        Args:
            size (int): size of the square
        """

        self.__size = size

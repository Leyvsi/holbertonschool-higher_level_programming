#!/usr/bin/python3
"""This module defines a class Square with a private size attribute.
"""

class Square:
"""Represents a square with a private size.
"""

   def __init__(self, size):
 """__init__ Construct the instance

        Args:
            size (int): Size of the square
 """
        self.__size = size

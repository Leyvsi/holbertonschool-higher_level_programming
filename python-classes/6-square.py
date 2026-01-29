#!/usr/bin/python3
"""This module defines a class Square with size, position, area, and printing."""


class Square:
    """Represents a square with size, position, and printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position.

        Args:
            size (int): size of the square (default 0)
            position (tuple): tuple of 2 positive integers (default (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (type(value) != tuple or len(value) != 2 or
            type(value[0]) != int or type(value[1]) != int or
            value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' character with position offsets.

        Prints an empty line if size is 0. 
        Position[0] = spaces before each line.
        Position[1] = number of new lines before the square.
        """
        if self.__size == 0:
            print()
            return
        # Vertical offset
        for _ in range(self.__position[1]):
            print()
        # Print each line of the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


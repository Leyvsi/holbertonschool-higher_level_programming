#!/usr/bin/python3
"""
Module defining the Square class.
Inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        # Validate size using the inherited integer_validator
        self.integer_validator("size", size)
        
        # Initialize the parent class (Rectangle)
        super().__init__(size, size)
        
        # Store size as a private attribute
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the print() and str() representation of the square.

        Returns:
            A string in the format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

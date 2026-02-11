#!/usr/bin/python3
"""
Module defining the Rectangle class.
Inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Validate width using inherited integer_validator
        self.integer_validator("width", width)
        self.__width = width

        # Validate height using inherited integer_validator
        self.integer_validator("height", height)
        self.__height = height

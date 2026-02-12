#!/usr/bin/python3
"""
This module demonstrates Duck Typing and Abstract Base Classes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class for different shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculates the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate area: pi * r^2
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate perimeter: 2 * pi * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate area: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate perimeter: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter of any object that behaves like a Shape.
    This is an example of Duck Typing.
    """
    # We call the methods without checking the object type
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

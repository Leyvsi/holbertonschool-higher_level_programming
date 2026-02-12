#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Base Class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        """
        # This method has no implementation here
        pass


class Dog(Animal):
    """
    Subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Implementation of the sound method for a dog.
        """
        # Returns the specific sound of a dog
        return "Bark"


class Cat(Animal):
    """
    Subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Implementation of the sound method for a cat.
        """
        # Returns the specific sound of a cat
        return "Meow"

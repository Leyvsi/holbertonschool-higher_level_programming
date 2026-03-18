#!/usr/bin/python3
"""
This module explores multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints habitat message."""
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints habitat message."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """Overrides the fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method."""
        print("The flying fish lives both in water and the sky!")

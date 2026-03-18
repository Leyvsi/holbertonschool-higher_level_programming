#!/usr/bin/python3
"""
This module defines mixins for swimming and flying, and a Dragon class.
"""


class SwimMixin:
    """
    Mixin to add swimming behavior.
    """

    def swim(self):
        """
        Prints a swimming message.
        """
        # Provides the swim capability
        print("The creature swims!")


class FlyMixin:
    """
    Mixin to add flying behavior.
    """

    def fly(self):
        """
        Prints a flying message.
        """
        # Provides the fly capability
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that combines multiple behaviors using mixins.
    """

    def roar(self):
        """
        Specific behavior for the dragon.
        """
        # Dragons roar, a unique ability not from mixins
        print("The dragon roars!")

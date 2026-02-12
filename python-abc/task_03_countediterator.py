#!/usr/bin/python3
"""
This module defines the CountedIterator class.
"""


class CountedIterator:
    """
    An iterator that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.
        """
        # Create an iterator from the provided iterable
        self.iterator = iter(iterable)
        # Counter to track items
        self.count = 0

    def get_count(self):
        """
        Return the current count of items iterated.
        """
        return self.count

    def __next__(self):
        """
        Fetch the next item and increment the counter.
        """
        try:
            # Try to get the next item from the internal iterator
            item = next(self.iterator)
            # If successful, increment the counter
            self.count += 1
            return item
        except StopIteration:
            # Re-raise the exception when the end is reached
            raise StopIteration

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

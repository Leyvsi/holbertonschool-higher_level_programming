#!/usr/bin/python3
"""
This module defines the VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A custom list that prints notifications when modified.
    """

    def append(self, item):
        """
        Add an item and print a notification.
        """
        # Call the original append method from the list class
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extend the list and print a notification with the count of items.
        """
        # Calculate how many items are being added
        count = len(x)
        # Call the original extend method
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Remove an item and print a notification before doing so.
        """
        # Notification must be printed before removal as per instructions
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item and print a notification. Defaults to the last item.
        """
        # Retrieve the item to be popped to display its value in the message
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

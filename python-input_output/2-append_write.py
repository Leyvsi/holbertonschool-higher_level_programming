#!/usr/bin/python3
"""
This module contains a function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.
    Returns the number of characters added.
    """
    # Open the file in append mode ('a')
    # This creates the file if it doesn't exist or adds to the end if it does
    with open(filename, "a", encoding="utf-8") as f:
        # Returns the number of characters added
        return f.write(text)

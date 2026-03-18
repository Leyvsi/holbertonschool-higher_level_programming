#!/usr/bin/python3
"""
This module contains a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF8 text file and returns the number of characters.
    """
    # Open the file in write mode ('w') which creates or overwrites it
    with open(filename, "w", encoding="utf-8") as f:
        # The write method returns the number of characters written
        return f.write(text)

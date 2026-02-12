#!/usr/bin/python3
"""
This module contains a function that reads a text file.
"""


def read_file(filename=""):
    """
    Reads a UTF8 text file and prints it to stdout.
    """
    # Open the file using the with statement for automatic cleanup
    with open(filename, encoding="utf-8") as f:
        # Read and print the content of the file
        print(f.read(), end="")

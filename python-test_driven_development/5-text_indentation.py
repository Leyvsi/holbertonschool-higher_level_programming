#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' or ':'.

    Raises TypeError if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0
    length = len(text)

    for i, char in enumerate(text):
        if char in separators:
            # print the segment trimmed
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    # print remaining text if any, no extra newline at end
    remainder = text[start:].strip()
    if remainder:
        print(remainder)

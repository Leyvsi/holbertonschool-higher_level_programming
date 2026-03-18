#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
    # Return empty list for non-positive n
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop to create each subsequent row up to n
    for i in range(1, n):
        # Every row starts with 1
        row = [1]
        # Get the previous row to calculate the current one
        prev_row = triangle[i - 1]

        # Each element is the sum of the two elements above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Every row ends with 1
        row.append(1)
        # Add the completed row to the triangle
        triangle.append(row)

    return triangle

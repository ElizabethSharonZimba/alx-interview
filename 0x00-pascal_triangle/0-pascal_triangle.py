#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    
    Args:
    - n: Integer, number of rows of Pascal's Triangle to generate
    
    Returns:
    - List of lists of integers representing Pascal’s Triangle up to the nth row
    - Returns an empty list if n <= 0
    """
    triangle = []
    
    if n > 0:
        for row_index in range(1, n + 1):
            row = []
            coefficient = 1
            for element_index in range(1, row_index + 1):
                row.append(coefficient)
                coefficient = coefficient * (row_index - element_index) // element_index
            triangle.append(row)
    
    return triangle

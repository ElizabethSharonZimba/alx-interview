#!/usr/bin/python3
"""
Test Rotate 2D Matrix
"""

from 0-rotate_2d_matrix import rotate_2d_matrix 

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    rotate_2d_matrix(matrix)

    print("\nRotated Matrix:")
    for row in matrix:
        print(row)


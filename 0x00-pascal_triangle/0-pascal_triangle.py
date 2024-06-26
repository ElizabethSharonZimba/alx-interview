#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    count = [[1]]
    for i in range(n - 1):
        track = [0] + count[-1] + [0]
        row = []
        for j in range(len(count[-1]) + 1):
            row.append(track[j] + track[j + 1])
        count.append(row)
    return count

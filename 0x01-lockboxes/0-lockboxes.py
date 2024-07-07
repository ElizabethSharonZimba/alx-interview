#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
        index += 1

    return len(setofkeys) == total_boxes

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes))  # True

    boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[0]]
    print(canUnlockAll(boxes))  # True

    boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]]
    print(canUnlockAll(boxes))  # False

    boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5]]
    print(canUnlockAll(boxes))  # False

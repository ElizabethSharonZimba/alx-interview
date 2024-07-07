#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    boxes is a list of lists, where each sublist represents keys in that box.
    The first box is always unlocked.
    """
    if not boxes or not isinstance(boxes, list) or not all(isinstance(box, list) for box in boxes):
        return False

    total_boxes = len(boxes)
    set_of_keys = {0}
    visited = {0}
    keys_to_visit = [0]

    while keys_to_visit:
        current_key = keys_to_visit.pop()
        for key in boxes[current_key]:
            if key not in visited and key < total_boxes:
                visited.add(key)
                set_of_keys.add(key)
                keys_to_visit.append(key)

    return len(visited) == total_boxes

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes))

    boxes = [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))

    boxes = [[0]]
    print(canUnlockAll(boxes))

    boxes = [[10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6]]
    print(canUnlockAll(boxes))  # Expected: True

    boxes = [[7, 5], [1, 10, 7], [9, 6, 10], [7, 9], [2], [7, 3], [7, 9, 10, 10, 8, 9, 2, 5], [7, 2, 2, 4, 4, 2, 4, 8, 7], [4, 2, 9, 6, 6, 5, 5]]
    print(canUnlockAll(boxes))  # Expected: False

    # Additional edge cases
    boxes = [[]]
    print(canUnlockAll(boxes))  # Expected: True (single box, already unlocked)

    boxes = [[], [0]]
    print(canUnlockAll(boxes))  # Expected: False (box 1 can't be opened)

    boxes = [[1], [0]]
    print(canUnlockAll(boxes))  # Expected: True (boxes are mutually unlocked)


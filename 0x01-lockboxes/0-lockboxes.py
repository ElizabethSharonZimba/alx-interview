#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Parameters:
    boxes (list of list of int): The list of boxes with keys inside them.
    
    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False
    
    n = len(boxes)
    keys = {0}
    opened = set()
    
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key not in keys and key < n:
                    keys.add(key)
                    queue.append(key)
    
    return len(opened) == n

if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  #True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  #  False


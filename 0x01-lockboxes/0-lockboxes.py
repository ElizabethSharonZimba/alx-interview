#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Function that checks if all boxes can be unlocked.
    Args:
        boxes: List of lists where each sublist contains keys to other boxes.
    Returns:
        True if all boxes can be unlocked, False otherwise.
    """
    keys = [0]
    total_boxes = len(boxes)
    
    for key in boxes[0]:
        if key < total_boxes and key not in keys and key > 0:
            keys.append(key)
    
    index = 0
    while index < len(keys):
        setkey = keys[index]
        for key in boxes[setkey]:
            if key < total_boxes and key not in keys and key > 0:
                keys.append(key)
        index += 1
    
    return len(keys) == total_boxes

#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    unlockboxes
    """
    total_boxes = len(boxes)
    keys = [0]
    counter = 0
    i = 0

    while i < len(keys):
        setkey = keys[i]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in keys:
                keys.append(key)
                counter += 1
        i += 1

    return counter == total_boxes - 1

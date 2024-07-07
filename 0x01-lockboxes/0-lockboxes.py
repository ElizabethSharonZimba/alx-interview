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

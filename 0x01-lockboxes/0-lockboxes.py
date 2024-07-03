#!/usr/bin/python3
def look_next_opened_box(opened_boxes):
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return True

    aux = {0: {'status': 'opened', 'keys': boxes[0]}}

    while True:
        keys = look_next_opened_box(aux)
        if keys:
            for key in keys:
                if key < len(boxes) and key not in aux:
                    aux[key] = {'status': 'opened', 'keys': boxes[key]}
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        else:
            break

    return len(aux) == len(boxes)

if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False


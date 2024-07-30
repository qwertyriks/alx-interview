#!/usr/bin/python3
"""0x01-lockboxes"""


def canUnlockAll(boxes):
    """
    1.taking boxes
    2.creating set of keys
    3.go to box 0
    4.getting all keys and add them setofkeys
    5.starting opening boxes from setofkeys
    6.go to each box of each keyand take the keys
    from it and add them to set of keys
    7.keep loping through all setof keys
    8.ignore keys that dont have box
    9.tracking opening of boxes by a counter, if at end it
    10.equal to lentgh of boxes it mean all boxes unlock
            OPTIMIZE IDEA :
                if we add 0 to setofkeys at start, we dont need for in 23
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1

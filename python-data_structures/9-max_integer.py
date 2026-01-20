#!/usr/bin/python3

def max_integer(l=[]):
    if len(l) == 0:
        return None
    max_val = l[0]
    for num in l[1:]:
        if num > max_val:
            max_val = num
    return max_val

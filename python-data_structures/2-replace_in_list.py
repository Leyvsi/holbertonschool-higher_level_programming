#!/usr/bin/python3

def replace_in_list(l, idx, element):
    if idx < 0 or idx >= len(l):
        return l
    l[idx] = element
    return l

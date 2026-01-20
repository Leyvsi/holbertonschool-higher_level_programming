#!/usr/bin/python3

def element_at(l, idx):
    if idx < 0 or idx >= len(l):
        return None
    return l[idx]

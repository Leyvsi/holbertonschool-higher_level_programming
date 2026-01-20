#!/usr/bin/python3

def delete_at(l=[], idx=0):
    if idx < 0 or idx >= len(l):
        return l
    del l[idx]
    return l

#!/usr/bin/python3
def new_in_list(l, idx, element):
    new_list = l [:]
    if idx < 0 or idx >= len(l):
        return new_list
    new_list[idx] = element
    return new_list

#!/usr/bin/python3

def divisible_by_2(l=[]):
    result = []
    for num in l:
        result.append(num % 2 == 0)
    return result

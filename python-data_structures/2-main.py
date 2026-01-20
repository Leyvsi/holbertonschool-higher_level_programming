#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

l = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(l, idx, new_element)

print(new_list)
print(l)

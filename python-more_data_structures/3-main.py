#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

set_3 = {"Python", "C", "Javascript"}
set_4 = {"Python", "C", "Ruby"}
c_set2 = common_elements(set_3, set_4)
print(sorted(list(c_set2)))

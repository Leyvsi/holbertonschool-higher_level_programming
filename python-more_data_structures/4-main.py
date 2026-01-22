#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
diff_set = only_diff_elements(set_1, set_2)
print(sorted(list(diff_set)))

set_3 = {"Python", "C", "Javascript"}
set_4 = {"Python", "C", "Ruby"}
diff_set2 = only_diff_elements(set_3, set_4)
print(sorted(list(diff_set2)))

#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

my_dict = {"a": 1, "b": 2, "c": 3}
print(number_keys(my_dict))

another_dict = {"name": "Holberton", "age": 19, "city": "Paris"}
print(number_keys(another_dict))

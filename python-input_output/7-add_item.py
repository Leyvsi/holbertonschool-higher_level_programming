#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list
and saves them to a JSON file.
"""
import sys
import os


# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file exists to decide whether to load it or start a new list
if os.path.exists(filename):
    # Load existing items from the file
    items = load_from_json_file(filename)
else:
    # Start with an empty list if file doesn't exist
    items = []

# Add all command line arguments to the list (excluding the script name)
# sys.argv[1:] captures everything after "./7-add_item.py"
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

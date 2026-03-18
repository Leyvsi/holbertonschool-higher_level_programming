import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    """
    # Open the file in write mode ('w'). 
    # If it exists, it will be overwritten.
    with open(filename, 'w', encoding='utf-8') as f:
        # Use json.dump to write the dictionary to the file
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.
    """
    # Open the file in read mode ('r')
    with open(filename, 'r', encoding='utf-8') as f:
        # Use json.load to read and convert the JSON back to a dict
        return json.load(f)

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Read data from a CSV file and convert it to a JSON file.
    """
    try:
        data_list = []

        # Open the CSV file for reading
        with open(csv_filename, 'r', encoding='utf-8') as csv_f:
            # Use DictReader to automatically map headers to dictionary keys
            reader = csv.DictReader(csv_f)
            for row in reader:
                data_list.append(row)

        # Open the JSON file for writing
        with open('data.json', 'w', encoding='utf-8') as json_f:
            # Serialize the list of dictionaries to JSON
            # indent=4 makes the file human-readable (optional but nice)
            json.dump(data_list, json_f, indent=4)

        return True

    except FileNotFoundError:
        # Return False if the CSV file does not exist
        return False
    except Exception:
        # Return False for any other unexpected error
        return False

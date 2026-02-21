from task_02_csv import convert_csv_to_json

# Define the source file
csv_file = "data.csv"

# Run the conversion
print(f"Converting {csv_file} to data.json...")
success = convert_csv_to_json(csv_file)

if success:
    print("Conversion was successful!")

    # Optional: Read and print the result to verify
    import json
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            print("\nContent of data.json:")
            print(data)
    except Exception as e:
        print(f"Error reading the output file: {e}")
else:
    print("Conversion failed. Check if data.csv exists.")

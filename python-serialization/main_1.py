from task_01_pickle import CustomObject

# Create object
original = CustomObject("John", 25, True)
print("Original:")
original.display()

# Serialize
original.serialize("object.pkl")

# Deserialize
recovered = CustomObject.deserialize("object.pkl")

if recovered:
    print("\nRecovered:")
    recovered.display()
else:
    print("\nFailed to recover object.")

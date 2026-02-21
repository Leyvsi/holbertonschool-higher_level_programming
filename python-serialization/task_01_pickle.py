import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialize the custom object with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a specific format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.
        """
        try:
            # 'wb' means Write Binary - pickle needs binary mode
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load an instance of CustomObject from a file.
        """
        try:
            # 'rb' means Read Binary
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            # Return None if the file is missing or corrupted
            return None

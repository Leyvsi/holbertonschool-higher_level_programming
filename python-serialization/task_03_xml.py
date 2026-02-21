import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    # Create the root element <data>
    root = ET.Element("data")

    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure value is converted to string for XML

    # Create an ElementTree object and write it to the file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Read an XML file and deserialize it back into a Python dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        # This basic version assumes a flat dictionary structure
        return {child.tag: child.text for child in root}

    except (FileNotFoundError, ET.ParseError):
        # Return None if file is missing or XML is invalid
        return None

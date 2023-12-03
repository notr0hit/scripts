import re

def parse_data(file_path):
    # Define the file path

    data = ''
    # Read the data from the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Define a regular expression pattern to match email:password pairs
    pattern = r'([\w\.-]+@[\w\.-]+):([^\s]+)'

    # Use regular expression to find all email:password pairs
    matches = re.findall(pattern, data)

    # Create a list of dictionaries containing email and password
    credentials = [{'email': match[0], 'password': match[1]} for match in matches]

    # Print the extracted credentials
    return credentials

import sys  # Importing sys for command-line argument handling

def main():
    """
    Main function to count the number of non-empty, non-comment lines in a Python file.
    """
    count_lines = 0  # Initialize a counter for valid lines
    pyfile = valid_file()  # Validate and retrieve the Python file name

    try:
        # Open the specified Python file for reading
        with open(pyfile) as aFile:
            row_list = aFile.readlines()  # Read all lines from the file

            # Process each line to check if it is a valid line
            for row in row_list:
                # Strip leading/trailing whitespace and remove newline characters
                row = row.strip().replace('\n', '')

                # Count the line if it's not a comment and not empty
                if not row.startswith("#") and not row == '':
                    count_lines += 1
    except FileNotFoundError:
        # Handle the case where the file does not exist
        sys.exit('File does not exist')
    
    # Print the total count of valid lines
    print('Number of lines:', count_lines)

def valid_file():
    """
    Validate the command-line arguments and check the provided file name.
    """
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        # Check if the file name has a '.py' extension
        if not sys.argv[1].endswith('.py'):
            sys.exit('Not a Python file')
        
        # Return the valid Python file name
        return sys.argv[1]

# Entry point of the script
if __name__ == '__main__':
    main()

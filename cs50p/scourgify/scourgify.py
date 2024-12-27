import sys  # Import sys module to handle command-line arguments
import csv  # Import csv module to read and write CSV files

def main():
    # Initialize an empty list to store the transformed data
    new_data = []
    
    # Read the old data from the input file
    old_data = read_file()
    
    # Process each dictionary (representing a row) in the old data
    for dictionary in old_data:
        # Split the 'name' field into last and first name
        name1, name2 = dictionary['name'].split(',')
        
        # Create a new dictionary with 'last', 'first', and 'house' fields
        new_data.append({'last': name1.lstrip(), 'first': name2.lstrip(), 'house': dictionary['house']})
    
    # Write the processed data to the output file
    write_file(new_data)

def read_file():
    # Check if the number of command-line arguments is valid
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')  # Exit if more than two arguments are passed
    elif len(sys.argv) < 3:
        sys.exit('Too few arguments')  # Exit if fewer than two arguments are passed
    
    # Validate that both arguments (input file and output file) are CSV files
    for files in sys.argv[1:]:
        if not '.csv' in files:
            sys.exit(f'{files} is not a CSV file')  # Exit if any file is not a CSV file
    
    try:
        lines_list = []  # Initialize an empty list to store the rows from the CSV
        # Open the input CSV file in read mode
        with open(sys.argv[1]) as aFile:
            reader = csv.DictReader(aFile)  # Create a CSV DictReader to parse the file into dictionaries
            for lines in reader:
                lines_list.append(lines)  # Add each row (as a dictionary) to the lines_list
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')  # Exit if the input file is not found
    
    # Return the list of rows read from the CSV file
    return lines_list

def write_file(dict_list):
    # Open the output CSV file in write mode
    with open(sys.argv[2], 'w') as aFile:
        # Create a CSV DictWriter to write the processed data
        writer = csv.DictWriter(aFile, fieldnames=['first', 'last', 'house'], lineterminator='\n')
        
        writer.writeheader()  # Write the header row with 'first', 'last', and 'house' as column names
        writer.writerows(dict_list)  # Write the processed data rows to the output file

# Ensure that the script runs only if executed directly (not imported as a module)
if __name__ == '__main__':
    main()  # Call the main function to execute the program
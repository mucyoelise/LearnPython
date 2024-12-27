from tabulate import tabulate  # Import the tabulate module to format data as a table
import sys  # Import sys module to handle command-line arguments
import csv  # Import csv module to handle reading CSV files

def main():
    # Get the data from the CSV file
    data_list = getfile_file_data()
    
    # Format the data into a table with headers from the keys in the data dictionary
    well_format = tabulate(tabular_data=data_list, headers='keys', tablefmt='grid')
    
    # Print the formatted table to the console
    print(well_format)

def getfile_file_data():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) > 2 :
        sys.exit('Too many arguments')  # Exit the program if more than one argument is provided
    elif len(sys.argv) < 2:
        sys.exit('Too few arguments')  # Exit the program if no argument is provided
    
    # Check if the file provided as argument is a CSV file
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')  # Exit the program if the file is not a CSV file
    else:
        row_list = list()  # Initialize an empty list to store the rows of the CSV file
        try:
            # Open the file provided in the command-line argument
            with open(sys.argv[1]) as aFile:
                reader = csv.DictReader(aFile)  # Create a CSV DictReader to read the file into dictionaries
                for line in reader:
                    row_list.append(line)  # Append each row to the list as a dictionary
        except FileNotFoundError:
            sys.exit('File does not exist')  # Exit if the file does not exist
    return row_list  # Return the list of rows

# Ensure that the script runs only if it's executed directly, not imported as a module
if __name__ == '__main__':
    main()  # Call the main function to execute the program
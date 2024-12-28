#-----------Reading the file using WITH operator to open the file----------------

# Initialize an empty list to store the data
file_list = []

# Use the 'with' statement to open the file safely; it automatically closes the file after the block is executed
with open('Book1.csv') as file:
    # Read the file line by line
    for line in file:
        print(line.strip())  # Print each line after removing leading/trailing whitespace
        
        # Split the line by comma, extracting the name and telephone
        names, telephone = line.split(',')  # This assumes each line has two parts (name, telephone)
        
        # Append the tuple (name, telephone) to the file_list
        file_list.append((names, telephone.strip()))  # Strip the telephone value of any extra whitespace

# After processing the file, print the list of tuples that contains the data from the CSV
print('\n------------Reading file into the list of tuples:--------------------')
print(f'\n{file_list}')  # Print the list of tuples containing name and telephone numbers
print()  # Print an empty line for separation
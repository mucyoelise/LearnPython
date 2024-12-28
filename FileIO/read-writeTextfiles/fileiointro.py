# Opening the file 'student_info.txt' in read mode ('r')
student_file = open('student_info.txt', 'r')

# Initialize a counter variable to keep track of line numbers
counter = 1

# Loop through each line in the file
for line in student_file:
    # Print the line number and the line content after stripping leading/trailing whitespaces
    print(f'Line {counter}: {line.strip()}') 
    # The .strip() method removes any unwanted whitespace characters (e.g., \n at the end of the line)
    
    # Increment the counter by 1 to keep track of line numbers
    counter += 1

# Print an empty line for output formatting
print()

# Close the file after reading its contents
student_file.close()
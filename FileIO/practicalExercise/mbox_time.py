time_list = list()  # Initialize an empty list to store the extracted hours from the emails

# Open the file specified by the user and process it line by line
with open(input('Enter file name: ')) as file:  # Using 'with' to automatically close the file after reading
    for line in file:  # Read each line of the file
        if line.startswith('From '):  # Check if the line starts with 'From '
            # Extract the time (the second-to-last word in the line) and append to the time_list
            time_list.append(line.split()[len(line.split())-2])

# Create a sorted list of hours by splitting the time in the 'time_list' and selecting the hour (before the colon)
hour_list = sorted([hour.split(':')[0] for hour in time_list])  # Extract hours and sort them

# Create a dictionary with the hours as keys and their occurrences as values
hour_dict = {hour: hour_list.count(hour) for hour in hour_list}  # Count occurrences of each hour

# Iterate through the dictionary and print the hour and its occurrence
for hour, occurance in hour_dict.items():
    print(f'{hour} {occurance}')  # Print the hour and its occurrence in the format: 'hour occurrence'

#----------------You can check for the following codes also.(Both do the same)-------------------------

'''
time_list = list()
with open(input('Enter file name: ')) as file:
    for line in file:
        if line.startswith('From '):
            time_list.append(line.split()[len(line.split())-2])
hour_list = [hour.split(':')[0] for hour in time_list ]
hour_tuple_dict = sorted({hour : hour_list.count(hour) for hour in hour_list}.items())
for hour, occurance in hour_tuple_dict:
    print(f'{hour} {occurance}')
print(dir(tuple()))

'''

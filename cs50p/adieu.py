# Initialize an empty list to store names and an empty string for the formatted output
name_list = list()
format_string = str()

# Infinite loop to collect user input
while True:
    try:
        # Prompt the user for a name, capitalize the first letter, and append it to the list
        prompt = input('Name: ').capitalize()
        name_list.append(prompt)
    except KeyboardInterrupt:
        # Exit the input loop gracefully when the user presses Ctrl+C
        print()  # Print a newline for better formatting
        break

# Process the list of names to create a formatted string
while True:
    if len(name_list) == 1:  # Case when there is only one name
        for name in name_list:
            format_string = name  # The formatted string is just the single name
        break
    elif len(name_list) == 2:  # Case when there are exactly two names
        # Combine the two names with "and"
        format_string = name_list[0] + ' and ' + name_list[1]
        break
    else:  # Case when there are more than two names
        # Insert "and" before the last name
        name_list.insert(len(name_list) - 1, 'and')
        for ind, name in enumerate(name_list):
            # Before "and", add names separated by commas
            if not ind >= name_list.index('and'):
                format_string = format_string + name + ', '
            else:
                # After "and", add names with a space instead of a comma
                format_string = format_string + name + ' '
        break

# Print the final formatted farewell message
print(f'Adieu, adieu, to {format_string.strip()}')
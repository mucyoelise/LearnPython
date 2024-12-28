# Prompt the user to input the file name
name = input('Enter file name: ')  
emails_list = list()  # Initialize an empty list to store emails

# Try to open the file with the provided name
try:
    file = open(name)  # Open the file in read mode
except:
    print("File can't open, check and try again later!")  # If the file can't be opened, print an error message
    exit()  # Exit the program if the file cannot be opened

# Read the file line by line
for line in file:
    if line.startswith('From '):  # Check if the line starts with 'From '
        email = line.split()[1]  # Split the line into words and get the second word (the email address)
        emails_list.append(email)  # Append the email to the emails_list

file.close()  # Close the file after reading

# Create a dictionary to count the occurrences of each email in the list
data_dict = {email: emails_list.count(email) for email in emails_list}  # Dictionary comprehension to count occurrences

# Loop through the dictionary and find the email with the highest occurrence
for email, occurance in data_dict.items():
    if occurance == max(data_dict.values()):  # Check if the current email has the maximum number of occurrences
        print(f'An email sends the greatest number of mail message is: {email} with {occurance} messages.')  
        # Print the email with the greatest number of messages and how many times it appeared
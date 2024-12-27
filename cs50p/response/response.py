import validator_collection  # Importing the validator_collection library to use its email validation function

def main():
    # Prompt the user to input their email address and validate it
    print(validate_email(input("What's your email address? ")))

def validate_email(s: str):
    # Check if the provided string is a valid email using the 'is_email' function from validator_collection
    return 'Valid' if validator_collection.is_email(s) else 'Invalid'  # Return 'Valid' if the email is valid, otherwise 'Invalid'

# Ensure the main function is executed when the script is run directly
if __name__ == '__main__':
    main()  # Call the main function to start the program
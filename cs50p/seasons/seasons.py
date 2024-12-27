import sys  # Import sys for handling program exit
from datetime import date  # Import date to work with date objects
from inflect import engine  # Import engine from the inflect library to convert numbers to words

class TimeCalc():
    # Initialize the TimeCalc class with a date
    def __init__(self, date):
        self.date = date  # Store the date object
    
    # Overload the subtraction operator to calculate the difference between two TimeCalc objects
    def __sub__(self, other):
        return f'{self.date - other.date}'  # Subtract the dates and return the difference as a string

    # Represent the object as a human-readable string in words
    def __repr__(self):
        # Convert the date value (in minutes) to words
        output = engine().number_to_words(num=self.date, andword='')
        return f'{output.capitalize()} minutes'  # Format the output string to display minutes

def main():
    today = TimeCalc(date.today())  # Create a TimeCalc object for today's date

    try:
        # Prompt user for date of birth and convert the input string to a date object
        input_date = date.fromisoformat(input('Date of Birth: '))  
        dob = TimeCalc(date=input_date)  # Create a TimeCalc object for the user's date of birth
    except ValueError:
        sys.exit(f'Invalid input')  # Exit the program if the date format is incorrect
    
    # Calculate the difference between today's date and the user's date of birth
    user_days = today - dob

    # Extract the number of days from the string (format: "XX days, XX hours, XX minutes")
    user_days_part = user_days.split(',')[0]
    user_days_int = int(user_days_part.split()[0])  # Convert the number of days to an integer

    # Convert the number of days into minutes (1 day = 24 hours * 60 minutes)
    user_min_int = user_days_int * 24 * 60

    # Create a TimeCalc object to convert the number of minutes into words
    user_min_word = TimeCalc(user_min_int)

    # Print the result: the number of minutes in words
    print(user_min_word)

if __name__ == '__main__':
    main()  # Call the main function to execute the program
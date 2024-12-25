import random  # Importing random for generating random numbers

def main():
    """
    Main function to execute the math quiz.
    """
    level = get_level()  # Get the difficulty level from the user
    user_marks = 0  # Initialize the score counter

    # Loop to generate 10 questions
    for questions in range(10):
        # Generate two random integers based on the difficulty level
        x = generate_integer(level)
        y = generate_integer(level)
        
        # Allow up to 3 attempts for each question
        for i in range(4):
            if not i == 3:
                # Prompt the user to solve the question
                print(f'{x} + {y} = ', end=" ")
                if x + y == get_answer():  # Check if the answer is correct
                    user_marks += 1  # Increment score for a correct answer
                    break  # Exit the loop for this question
                else: 
                    print('EEE')  # Print an error message for a wrong answer
                    continue  # Allow another attempt
            # After 3 wrong attempts, display the correct answer
            print(f'{x} + {y} = {x + y}')
    
    # Print the final score
    print(f'Score: {user_marks}')

def get_level():
    """
    Prompt the user to select a difficulty level (1, 2, or 3).
    """
    while True:
        try:
            user_level = int(input('Level: '))  # Get the level from the user
            if user_level in (1, 2, 3):  # Ensure the level is valid
                return user_level
        except ValueError:
            # Ignore invalid inputs and prompt again
            pass

def generate_integer(user_level):
    """
    Generate a random integer based on the specified difficulty level.
    """
    low_nbr = 10 * (user_level - 1)  # Calculate the lower bound
    high_nbr = (10**user_level) - 1  # Calculate the upper bound
    return random.randint(low_nbr, high_nbr)  # Return a random number within the range

def get_answer():
    """
    Get the user's answer to a question. Returns None for invalid input.
    """
    try:
        return int(input())  # Try to convert the input to an integer
    except:
        # Return None if the input is invalid
        pass

# Entry point of the script
if __name__ == "__main__":
    main()
def main():
    """
    Main function to execute the guessing game.
    """
    # Prompt the user to input the level (upper limit for the random number)
    user_level = prompt_level()
    
    # Generate a random number within the specified level
    random_guess = get_random_guess(user_level)
    
    while True:
        # Prompt the user to guess the number
        user_guess = prompt_guess()
        
        # Check if the guess matches the random number
        if user_guess == random_guess:
            print('Just right!')  # Correct guess message
            exit()  # Exit the program
        elif user_guess > random_guess:
            print('Too large!')  # Message for a guess that's too high
            continue  # Continue to the next iteration of the loop
        elif user_guess < random_guess:
            print('Too small!')  # Message for a guess that's too low
            continue  # Continue to the next iteration of the loop

def prompt_level():
    """
    Prompt the user to input a valid level (upper limit for the random number).
    Ensures the input is a positive integer greater than 1.
    """
    while True:
        try:
            # Prompt the user for the level
            level = int(input('Level: '))
            
            # Ensure the level is greater than 1
            if level <= 1:
                continue
            
            return level  # Return the valid level
        except ValueError:
            # Ignore invalid inputs and prompt again
            pass

def prompt_guess():
    """
    Prompt the user to input a valid guess.
    Ensures the input is a positive integer greater than 1.
    """
    while True:
        try:
            # Prompt the user for their guess
            guess = int(input('Guess: '))
            
            # Ensure the guess is greater than 1
            if guess <= 1:
                continue
            
            return guess  # Return the valid guess
        except ValueError:
            # Ignore invalid inputs and prompt again
            pass

def get_random_guess(user_input):
    """
    Generate a random integer between 1 and the user-provided level (inclusive).
    """
    import random  # Import the random module for generating random numbers
    try:
        return random.randint(1, user_input)  # Generate a random number
    except ValueError:
        return False  # Return False if the input level is invalid

# Entry point of the program
main()
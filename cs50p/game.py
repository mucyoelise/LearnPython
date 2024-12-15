def main():
    user_level = prompt_level()
    random_guess = get_random_guess(user_level)
    while True:
        user_guess = prompt_guess()
        if user_guess == random_guess:
            print('Just right!')
            exit()
        elif user_guess > random_guess:
            print('Too large!')
            continue
        elif user_guess < random_guess:
            print('Too small!')
            continue

def prompt_level():
    while True:
        try:
            level = int(input('Level: '))
            if level <= 1:
                continue
            return level
        except ValueError:
            pass

def prompt_guess():
    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 1:
                continue
            return guess
        except ValueError:
            pass

def get_random_guess(user_input):
    import random
    try:
        return random.randint(1, user_input)
    except ValueError:
        return False
main()
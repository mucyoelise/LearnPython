from random import choice
def random_word_picker():
    with open("words.txt", "r") as file:
        word_list = file.read().split()
    return choice(word_list)

secret_word = random_word_picker()
guessed_word = ["-"] * len(secret_word)
letters_not_used = set("abcdefghijklmnopqrstuvwxyz")
trials = 10
warnings = 3

print("\nPLAY HANGMAN GAME!!")
print(f"\nThe secret word contains {len(secret_word)} letters.")

while trials > 0 and "-" in guessed_word:
    print(f"Guesses and Warnings you remain are: {trials} and {warnings} respectively!")
    print(f"Letters not yet used: {' '.join(sorted(letters_not_used))}")
    print(f"Current guessed word: {' '.join(guessed_word)}")
    guess = input("Please guess a letter: ").lower()
    
    if not guess.isalpha() or len(guess) != 1:
        if warnings > 0:
            warnings -= 1
            print("\nYou entered a non-letter symbol. Therefore, you lose a warning.")
        else:
            trials -= 1
            print("\nYou entered a non-letter symbol. Therefore, you lose a guess.")
        continue
    
    if not guess in letters_not_used:
        if warnings > 0:
            warnings -= 1
            print("\nYou've already guessed that letter. Therefore, you lose a warning.")
        else:
            trials -= 1
            print("\nYou've already guessed that letter. Therefore, you lose a guess.")
        continue
    
    letters_not_used.discard(guess)
    
    if guess in secret_word:
        print("\nGood guess!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("\nSorry, that letter is not in the word.")
        trials -= 2 if guess in "aeiou" else 1

if "-" not in guessed_word:
    print(f"Congratulations, you WIN! The word was {secret_word}.")
    score = trials * len(set(secret_word))
    print(f"Your score: {score}")
else:
    print(f"You lost because all the guesses are exhausted.")
    print(f"----------The word was: {secret_word} ------------")
    
print()
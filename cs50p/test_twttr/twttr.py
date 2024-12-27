def main():
    # Get user input for the word to shorten
    word = input("Input: ")
    # Print the shortened version of the input word
    print(f"Output: {shorten(word)}")

def shorten(word):
    # Initialize an empty string to hold the shortened word
    shorten_word = str()
    # Iterate through each character in the word
    for char in word:
        # If the character is not a vowel (case insensitive), add it to the shortened word
        if char.lower() not in 'aeuio':
            shorten_word += char 
    # Return the shortened word (with vowels removed)
    return shorten_word

# Ensure the program runs only when executed directly, not when imported
if __name__ == '__main__':
    main()
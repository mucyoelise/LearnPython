import re

def main():
    # Prompts the user for input and passes the input string to the count function.
    print(count(input("Text: ")))

def count(s):
    # Uses the re.findall() function to find all occurrences of the word "um" (case-insensitive)
    # The word boundary (\b) ensures that we only match "um" as a complete word, not part of another word.
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    
    # Returns the number of matches found, which is the count of occurrences of "um" in the string.
    return len(matches)

if __name__ == "__main__":
    # Calls the main function when the script is executed directly.
    main()
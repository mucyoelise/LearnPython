def main():
    # Prompt the user for a plate input.
    plate = input("Plate: ")
    # Check if the plate is valid by calling the is_valid function.
    if is_valid(plate):
        print("Valid")  # If the plate is valid, print "Valid".
    else:
        print("Invalid")  # If the plate is not valid, print "Invalid".

def is_valid(s:str):
    # Check the length of the string to be between 2 and 6 characters.
    # Also, ensure the string is in uppercase.
    if not 2 <= len(s) <= 6 or not s.isupper():
        return False  # If the conditions aren't met, return False.

    # Loop through the string to check each character.
    for i, char in enumerate(s):
        try:
            # If the character is a number, check certain conditions.
            int(char)
            # If the number is at the beginning or it is '0', return False.
            if i < 2 or char == '0':
                return False
            else:
                # Find the index of the number in the string.
                nbrInd = s.find(char)
                # Call is_nbr_btn function to validate the number part after the first two characters.
                return is_nbr_btn(nbrInd, s)
        except:
            # If the character is not a number and it is the last character, return True.
            if i == len(s) - 1:
                return True
            pass  # Ignore the error and continue checking other characters.

def is_nbr_btn(index:int, string:str):
    # Get the substring from the current index to the end of the string.
    numbers = string[index:]
    try:
        # Check if the substring contains only numbers.
        int(numbers)
        return True  # If it's a valid number, return True.
    except:
        return False  # If it's not a valid number, return False.

if __name__ == '__main__':
    main()  # Call the main function to execute the program.
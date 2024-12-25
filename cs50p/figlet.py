import sys  # For handling command-line arguments
import pyfiglet  # For text formatting using ASCII art
import random  # For selecting a random font

def main():
    # Check if no command-line arguments are provided
    if len(sys.argv) == 1:
        # Call the program to use a random font
        print(random_font_program())
    else:
        # Call the program to customize the font based on user input
        print(customize_font_program())

def random_font_program():
    """
    Generates ASCII art text using a random font.
    """
    # Choose a random font from the available pyfiglet fonts
    random_font = random.choice(pyfiglet.Figlet().getFonts())
    # Get user input for the text to be formatted
    input_text = input('Input text to be formatted: ')
    # Generate ASCII art text with the random font and return it
    return pyfiglet.Figlet(font=random_font).renderText(input_text)

def customize_font_program():
    """
    Generates ASCII art text using a user-specified font.
    """
    # Validate that the first command-line argument is -f or --f
    if not (sys.argv[1] == '-f' or sys.argv[1] == '--f'):
        sys.exit(f"Usage: -f or --f not {sys.argv[1]}")  # Exit with usage instructions

    # Get the user-specified font name from the second command-line argument
    preferred_font = sys.argv[2]
    
    # Check if the specified font is available in pyfiglet's supported fonts
    if preferred_font not in pyfiglet.Figlet().getFonts():
        # Print error message if the font is unsupported
        print('Fatal: Make sure you have typed a font supported by the pyfiglet module')
        sys.exit("Usage: python <file-name>.py <-f or --f> <font-name>")  # Exit with usage instructions

    # Get user input for the text to be formatted
    input_text = input('Input text to be formatted: ')
    # Generate ASCII art text with the specified font and return it
    return pyfiglet.Figlet(font=preferred_font).renderText(input_text)

# Entry point of the script
main()
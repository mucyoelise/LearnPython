# ........Try to use command-line arguments to customize the fonts to be used......
# Use command-line arguments like (-f or --f) on argv[1] and (font-name) on argv[2]
import sys
import pyfiglet
import random
def main():
    if len(sys.argv) == 1:
        print(random_font_program())

    else:
        
        print(customize_font_program())

def random_font_program():
    random_font = random.choice(pyfiglet.Figlet().getFonts())
    return f'{pyfiglet.Figlet(random_font).renderText(input('Input text to be formatted: '))}'

def customize_font_program():
    if not sys.argv[1] == '-f' or sys.argv[1] == '--f':
        sys.exit(f"Usage: -f or --f not {sys.argv[1]}")
    preferred_font = sys.argv[2]
    if not preferred_font in pyfiglet.Figlet().getFonts():
        print('Fatal: Make sure you have typed the font supported in pyfiglet module')
        sys.exit("Usage: python <file-name>.py <-f or --f> <font-name>")        
    return f'{pyfiglet.Figlet(font=preferred_font).renderText(input('Input text to be formatted: '))}'

main()
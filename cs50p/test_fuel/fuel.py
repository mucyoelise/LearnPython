def main():
    # Prompt the user to input a fraction as a string (e.g., "3/4")
    fract = input('Fraction: ')
    # Convert the input fraction to a percentage
    get_perc = convert(fraction=fract)
    # Display the corresponding fuel gauge value based on the calculated percentage
    print(gauge(get_perc))

def convert(fraction):
    # Split the fraction string into numerator and denominator
    numer, denom = fraction.split('/')
    try:
        # Convert the numerator and denominator to float to handle decimal values
        numer = float(numer)
        denom = float(denom)
    except:
        # If the conversion fails (e.g., input is non-numeric), raise a ValueError
        raise ValueError()
    
    # Ensure both numerator and denominator are integers (whole numbers)
    if not numer.is_integer() or not denom.is_integer():
        raise ValueError()
    
    # Check if the denominator is zero (to prevent division by zero)
    if denom == 0:
        raise ZeroDivisionError()
    
    # Ensure that the numerator is not greater than the denominator (invalid fraction)
    if numer > denom:
        raise ValueError()
    
    # Calculate the percentage as a whole number (rounded to the nearest integer)
    return round((numer / denom) * 100)

def gauge(percentage):
    # If the percentage is 1 or less, return "E" for empty
    if percentage <= 1:
        return 'E'
    # If the percentage is 99 or more, return "F" for full
    elif percentage >= 99:
        return 'F'
    # Otherwise, return the percentage followed by a '%' sign
    else:
        return f'{percentage}%'

# This ensures that the main function is called only if the script is run directly (not imported)
if __name__ == "__main__":
    main()
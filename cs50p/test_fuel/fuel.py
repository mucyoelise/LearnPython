def main():

    fract = input('Fraction: ')
    get_perc = convert(fraction= fract)
    print(gauge(get_perc))

def convert(fraction):
    numer, denom = fraction.split('/')
    try:
        numer = float(numer)
        denom = float(denom)
    except:
        raise ValueError()
    
    if not numer.is_integer() or not denom.is_integer():
        raise ValueError()
    if denom == 0:
        raise ZeroDivisionError()
    if numer>denom:
        raise ValueError()
    
    return round((numer/denom) * 100)

def gauge(percentage):
    
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'

if __name__ == "__main__":
    main()

# Import the functions to be tested and the pytest module.
from fuel import convert, gauge
import pytest

# Define the main function to run the tests.


def main():
    # Run the test functions.
    test_convert()
    test_gauge()
    test_zero_division()
    test_value_error()

# Define the test for zero division.


def test_zero_division():
    # Check if the function raises a ZeroDivisionError as expected.
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

# Define the test for value error.


def test_value_error():
    # Check if the function raises a ValueError as expected.
    with pytest.raises(ValueError):
        convert("one/two")

# Define the test for valid conversions.


def test_convert():
    # Test valid conversions and expected outputs.
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_gauge():
    # Test various gauge values and expected "E" outputs.
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    # Test various gauge values and expected "F" outputs.
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    # Assert that gauge(50) returns the expected percentage string "50%"
    assert gauge(50) == "50%"
    # Assert that gauge(75) returns the expected percentage string "75%"
    assert gauge(75) == "75%"


# Run the main function if this script is executed directly.
if __name__ == "__main__":
    main()
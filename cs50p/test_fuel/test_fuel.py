from fuel import convert, gauge
import pytest

#------- Testing Errors----------

# Test for ValueError when the input is invalid
def test_valueError():
    # Check if ValueError is raised for non-numeric or invalid input
    with pytest.raises(ValueError):
        convert("one/two")  # Invalid input: words instead of numbers
        convert("1.5/3")     # Invalid input: decimal values
        convert("2/1")       # Invalid input: numerator > denominator

# Test for ZeroDivisionError when the denominator is zero
def test_zeroDivError():
    # Check if ZeroDivisionError is raised when the denominator is zero
    with pytest.raises(ZeroDivisionError):
        convert("2/0")  # Invalid input: division by zero

#-------- Testing convert function -----------

# Test for correct conversion of valid fraction inputs to percentage
def test_convert_arg():
    assert convert('3/4') == 75    # 3 divided by 4 equals 0.75, which is 75%
    assert convert('1/4') == 25    # 1 divided by 4 equals 0.25, which is 25%
    assert convert('4/4') == 100   # 4 divided by 4 equals 1.0, which is 100%

#-------- Testing gauge function --------------

# Test for correct output from the gauge function for various percentages
def test_gauge_arg():
    assert gauge(75) == '75%'   # Check for middle percentage (should return the percentage as a string)
    assert gauge(25) == '25%'   # Check for low percentage (should return the percentage as a string)
    assert gauge(100) == 'F'    # Check for full tank (100% should return 'F')
    assert gauge(0) == 'E'      # Check for empty tank (0% should return 'E')
    assert gauge(1) == 'E'      # Check for almost empty tank (1% should return 'E')
    assert gauge(99) == 'F'     # Check for almost full tank (99% should return 'F')
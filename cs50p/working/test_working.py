import pytest
from working import convert

## ------------ Testing invalid inputs -------------
def test_errors():
    # Test: Input with incorrect time format (hours and minutes separated by a colon, with "AM - PM" format)
    with pytest.raises(ValueError):
        convert('10:7 AM - 5:1 PM')

    # Test: Input with missing minutes after hour (like '9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')

    # Test: Input with "to" instead of "AM to PM" format
    with pytest.raises(ValueError):
        convert('09:00 to 17:00')

    # Test: Input with no space between the time and AM/PM
    with pytest.raises(ValueError):
        convert('9AM 5PM')

    # Test: Invalid time values (like '8:60 AM' or '4:60 PM', which are not valid times)
    with pytest.raises(ValueError):
        convert('8:60 AM to 4:60 PM')

## ---------- Testing valid inputs --------------
def test_validinp():
    # Test: Valid time format with "AM to PM"
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

    # Test: Valid time format with hour and minute values provided in 12-hour format
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'

    # Test: Valid time conversion from PM to AM
    assert convert('8:00 PM to 8:00 AM') == '20:00 to 08:00'

    # Test: Conversion of standard office hours
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'

    # Test: Conversion with spaces in the input time format
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
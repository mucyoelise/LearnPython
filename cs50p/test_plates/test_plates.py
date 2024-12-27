from plates import is_valid

#------- Testing the length of the plate (wordLen) -------
def test_worldLen():
    # Test cases where the plate length is within the valid range (2-6 characters)
    assert is_valid('HELLO') == True  # Valid, length is 5
    assert is_valid('HI') == True  # Valid, length is 2
    assert is_valid('H') == False  # Invalid, length is 1

#------- Testing the first character of the plate (wordFirstChar) -------
def test_wordFirstChar():
    # Test cases where the first character is alphabetic and the rest are valid
    assert is_valid('HELLO') == True  # Valid, starts with an alphabetic character
    # Test cases where the first character is a number (invalid)
    assert is_valid('1HELLO') == False  # Invalid, starts with a number
    assert is_valid('A3AAA') == False  # Invalid, starts with a letter but followed by a number in the second position
    assert is_valid('63AAA') == False  # Invalid, starts with numbers

#------- Testing for punctuation in the plate (wordWithPunc) -------
def test_wordWithPunc():
    # Test cases where the plate contains punctuation (invalid)
    assert is_valid('HEY,23') == False  # Invalid, contains a comma
    assert is_valid('HEY 23') == False  # Invalid, contains a space
    assert is_valid('HEY.12') == False  # Invalid, contains a period
    assert is_valid('AB:12') == False  # Invalid, contains a colon
    assert is_valid('AB/45') == False  # Invalid, contains a slash

#------- Testing the placement of numbers in the plate (nbrPlacement) -------
def test_nbrPlacement():
    # Valid cases where numbers appear at the end of the plate
    assert is_valid('HEY123') == True  # Valid, numbers are placed after the first two characters
    assert is_valid('HEY12') == True  # Valid, numbers at the end and have less than or equal to 6 characters
    # Invalid cases where numbers appear at the beginning or in the middle
    assert is_valid('AB23EF') == False  # Invalid, numbers in the middle of the plate
    assert is_valid("AA") == True  # Valid, plate contains only letters (valid 2-letter plate)
    # Invalid cases where numbers are at the beginning
    assert is_valid("A2") == False  # Invalid, number is at the end but is at position 2
    assert is_valid("2A") == False  # Invalid, number is at the beginning

#------- Testing zero placement in the plate (zeroPlacement) -------
def test_zeroPlacement():
    # Valid plates with numbers and no leading zeros
    assert is_valid('HEY102') == True  # Valid, the number is after the first two characters
    assert is_valid('CS50') == True  # Valid, valid format with number at the end
    # Invalid plate with a leading zero in the number section
    assert is_valid('HEY012') == False  # Invalid, leading zero in the number part
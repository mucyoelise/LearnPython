from numb3rs import validate

# Test when input contains non-numeric words.
def test_wordArguments():
    assert validate('cat') == False  # Test case for a word input. It should return False, as "cat" is not a valid IPv4 address.
    assert validate('cat.dog.hen.cow') == False  # Test case with words in each segment. Invalid, so should return False.
    assert validate('cat.cat') == False  # Test case with words in each segment. Should return False as words are not valid.

# Test for valid and invalid positive number arguments.
def test_posNbrArguments():
    assert validate('12.12.12.12') == True  # Valid IPv4 address with all segments between 0 and 255. Expected result: True.
    assert validate('257.233.233.233') == False  # 257 is out of range (greater than 255), so it should return False.
    assert validate('255.255.0.255') == True  # Valid IPv4 address with correct ranges. Expected result: True.
    assert validate('25.25') == False  # Incomplete address, missing two segments. Should return False.
    assert validate("75.456.76.65") == False  # 456 is out of range (greater than 255), so should return False.
    assert validate('233.233.233.233.233') == False  # Too many segments (5 instead of 4). Expected result: False.

# Test for negative number arguments.
def test_negNbrArguments():
    assert validate('-12.-12.12.12') == False  # Negative numbers are invalid in IPv4 addresses, should return False.
    assert validate('-257.-233.233.233') == False  # Negative and out-of-range numbers. Should return False.
    assert validate('-255.-255.0.255') == False  # Negative numbers in the address should return False.
    assert validate('-25.-25') == False  # Incomplete address with negative numbers, should return False.
    assert validate('-233.233.-233.233.233') == False  # Negative numbers in multiple segments, should return False.

# Additional edge case for address with leading zeros.
def test_leadingZeros():
    assert validate('192.168.001.001') == False  # Leading zeros in segments are not allowed in IPv4. Expected result: False.
    assert validate('192.168.01.1') == False  # Another case of leading zeros in a segment. Should return False.

# Test with special characters (invalid characters in the address).
def test_specialCharacters():
    assert validate('192.168.#$@.1') == False  # Special characters are invalid in IPv4 addresses. Expected result: False.
from twttr import shorten

#------- Testing word arguments -------
def test_arguments_word():
    # Test with a word that contains both vowels and consonants
    assert shorten(word= 'KavamaHanga') == 'KvmHng'  # Valid, vowels 'a' and 'a' are removed
    # Test with a word that has repeated vowels
    assert shorten(word= 'Ommema') == 'mmm'  # Valid, vowels 'o', 'e' and 'a' are removed

#------- Testing number arguments -------
def test_arguments_nbr():
    # Test with a number string (should not remove anything as numbers are not vowels)
    assert shorten(word = '1234') == '1234'  # Valid, no vowels to remove
    # Test with a negative number string (should not remove anything as numbers are not vowels)
    assert shorten(word= '-1234') == '-1234'  # Valid, no vowels to remove

#------- Testing symbol arguments -------
def test_arguments_symbol():
    # Test with symbols, should not remove any characters as symbols are not vowels
    assert shorten(word= '!@##$%^') == '!@##$%^'  # Valid, no vowels to remove in symbols
    # Test with symbols and numbers mixed with letters (only vowels should be removed)
    assert shorten(word= 'note@12@') == 'nt@12@'  # Valid, vowels 'o' and 'e' are removed
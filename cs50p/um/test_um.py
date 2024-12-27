from um import count

def test_arg():
    # Test case 1: The string contains exactly one "um"
    assert count('um') == 1
    
    # Test case 2: The string contains one occurrence of "um" surrounded by other text
    assert count('Hello, um, world') == 1
    
    # Test case 3: The string contains "um" amidst punctuation marks
    assert count('This is, um.... CS50.') == 1
    
    # Test case 4: The string contains "Um" with ellipses, ensuring case-insensitive match
    assert count('Um... what are regular expressions?') == 1
    
    # Test case 5: The string contains two occurrences of "um"
    assert count('"Um, thanks, um, regular expressions make sense now."') == 2
    
    # Test case 6: The string contains "um" in different forms (including "umm") and different punctuation, testing multiple instances
    assert count('Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?') == 2
from bank import value  # Importing the 'value' function from the bank module

def test_arg_startswith_H():
    # Test case 1: Greeting starts with 'Hello' or 'hello'
    assert value('Hello') == 0      # Should return 0
    assert value('hello') == 0      # Should return 0
    
    # Test case 2: Greeting starts with 'Hey' or 'hey'
    assert value('Hey') == 20       # Should return 20
    assert value('hey') == 20       # Should return 20

def test_arg_notstartswith_H():
    # Test case: Greeting does not start with 'H' or 'h'
    assert value('Morning') == 100  # Should return 100
    assert value('Good morning') == 100  # Should return 100

def test_nbr_arguments():
    # Test case: Greeting is a number, not starting with 'H' or 'h'
    assert value('1234') == 100     # Should return 100
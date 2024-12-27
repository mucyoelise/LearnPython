from seasons import TimeCalc  # Import the TimeCalc class from the seasons module

# Create TimeCalc objects with specific minute values
check1 = TimeCalc(123)  # 123 minutes
check2 = TimeCalc(22)   # 22 minutes

def test_date_calculator_str():
    # Test if the string representation of check1 is correct
    assert str(check1) == "One hundred twenty-three minutes"
    
    # Test if the string representation of check2 is correct
    assert str(check2) == "Twenty-two minutes"
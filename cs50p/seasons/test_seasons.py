from seasons import TimeCalc

check1 = TimeCalc(123)
check2 = TimeCalc(22)

def test_date_calculator_str():
    assert str(check1) == "One hundred twenty-three minutes"
    assert str(check2) == "Twenty-two minutes"

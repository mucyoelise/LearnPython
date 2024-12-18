import math_calc

def test_positive_nbrs():
    for num in [2, 10, 24, 380]:
        assert math_calc.square(num) == num**2

def test_negative_nbrs():
    for num in [-2, -23, -133, -30]:
        assert math_calc.square(num) == num**2

def test_zero_nbr():
    assert math_calc.square(0) == 0

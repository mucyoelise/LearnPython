from fuel import convert,gauge
import pytest

#------- Testing Errors----------
def test_valueError():
    with pytest.raises(ValueError):
        convert("one/two")
        convert("1.5/3")
        convert("2/1")
        
def test_zeroDivError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

#-------- Testing convert function -----------
def test_convert_arg():
    assert convert('3/4') == 75
    assert convert('1/4') == 25
    assert convert('4/4') == 100

#-------- Testing gauge function --------------
def test_gauge_arg():
    assert gauge(75) == '75%'
    assert gauge(25) == '25%'
    assert gauge(100) == 'F'
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

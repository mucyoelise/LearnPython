from numb3rs import validate

def test_wordArguments():
    assert validate('cat') == False
    assert validate('cat.dog.hen.cow') == False
    assert validate('cat.cat') == False

def test_posNbrArguments():
    assert validate('12.12.12.12') == True
    assert validate('257.233.233.233') == False
    assert validate('255.255.0.255') == True
    assert validate('25.25') == False
    assert validate("75.456.76.65") == False
    assert validate('233.233.233.233.233') == False

def test_negNbrArguments():
    assert validate('-12.-12.12.12') == False
    assert validate('-257.-233.233.233') == False
    assert validate('-255.-255.0.255') == False
    assert validate('-25.-25') == False
    assert validate('-233.233.-233.233.233') == False

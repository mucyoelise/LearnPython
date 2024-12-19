from plates import is_valid

def test_worldLen():
    assert is_valid('HELLO') == True
    assert is_valid('HI') == True
    assert is_valid('H') == False

def test_wordFirstChar():
    assert is_valid('HELLO') == True
    assert is_valid('1HELLO') == False
    assert is_valid('A3AAA') == False
    assert is_valid('63AAA') == False

def test_wordWithPunc():
    assert is_valid('HEY,23') == False
    assert is_valid('HEY 23') == False
    assert is_valid('HEY.12') == False
    assert is_valid('AB:12') == False
    assert is_valid('AB/45') == False

def test_nbrPlacement():
    assert is_valid('HEY123') == True
    assert is_valid('HEY12') == True
    assert is_valid('AB23EF') == False
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False

def test_zeroPlacement():
    assert is_valid('HEY102') == True
    assert is_valid('CS50') == True
    assert is_valid('HEY012') == False
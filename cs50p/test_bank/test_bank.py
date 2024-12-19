from bank import value

def test_arg_startswith_H():
    assert value('Hello') == 0
    assert value('hello') == 0
    assert value('Hey') == 20
    assert value('hey') == 20

def test_arg_notstartswith_H():
    assert value('Morning') == 100
    assert value('Good morning') == 100

def test_nbr_arguments():
    assert value('1234') == 100
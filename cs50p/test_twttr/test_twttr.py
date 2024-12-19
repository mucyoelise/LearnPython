from twttr import shorten

def test_arguments_word():
    assert shorten(word= 'KavamaHanga') == 'KvmHng'
    assert shorten(word= 'Ommema') == 'mmm'

def test_arguments_nbr():
    assert shorten(word = '1234') == '1234'
    assert shorten(word= '-1234') == '-1234'

def test_arguments_symbol():
    assert shorten(word= '!@##$%^') == '!@##$%^'
    assert shorten(word= 'note@12@') == 'nt@12@'
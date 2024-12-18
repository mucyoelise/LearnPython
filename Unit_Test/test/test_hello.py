import hello

def test_default_arg():
    assert hello.greet() == 'Hello, world!'

def test_other_arg():
    for name in ['Mucyo','ELISE','SaMuEl']:
        assert hello.greet(name) == f'Hello, {name}!'

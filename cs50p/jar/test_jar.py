from jar import Jar
import pytest

def test_init_errors():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-3)

def test_init_valid():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(3)
    assert jar.capacity == 3
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    jar.deposit(3)
    assert jar.capacity == 12
    assert jar.size == 3

def test_withdraw():

    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)

    assert jar.capacity == 5
    assert jar.size == 2
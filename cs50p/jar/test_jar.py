# Import necessary libraries and the Jar class
from jar import Jar
import pytest

# Test invalid initialization with negative capacities.
def test_init_errors():
    with pytest.raises(ValueError):  # Expecting ValueError when negative capacity is passed.
        Jar(-1)
    with pytest.raises(ValueError):  # Expecting ValueError again for another negative capacity.
        Jar(-3)

# Test valid initialization of the Jar class with default and custom capacities.
def test_init_valid():
    jar = Jar()  # Initialize with default capacity (12).
    assert jar.capacity == 12  # Assert the default capacity is 12.
    assert jar.size == 0  # Assert that the initial number of cookies is 0.

    jar = Jar(3)  # Initialize with custom capacity (3).
    assert jar.capacity == 3  # Assert the capacity is 3.
    assert jar.size == 0  # Assert that the initial number of cookies is 0.

# Test the string representation (__str__) of the Jar class.
def test_str():
    jar = Jar()  # Initialize an empty jar.
    assert str(jar) == ""  # Assert the string representation is empty when there are no cookies.

    jar.deposit(1)  # Deposit 1 cookie.
    assert str(jar) == "🍪"  # Assert that the string now shows 1 cookie.

    jar.deposit(11)  # Deposit 11 more cookies.
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # Assert the string shows 12 cookies in total.

# Test the deposit method to add cookies to the jar.
def test_deposit():
    jar = Jar()  # Initialize an empty jar.

    jar.deposit(3)  # Deposit 3 cookies.
    assert jar.capacity == 12  # Assert the capacity remains the same.
    assert jar.size == 3  # Assert that the number of cookies is now 3.

# Test the withdraw method to remove cookies from the jar.
def test_withdraw():
    jar = Jar(5)  # Initialize a jar with capacity 5.
    jar.deposit(5)  # Deposit 5 cookies to fill the jar.
    jar.withdraw(3)  # Withdraw 3 cookies.

    assert jar.capacity == 5  # Assert the capacity remains the same.
    assert jar.size == 2  # Assert the jar now contains 2 cookies after the withdrawal.
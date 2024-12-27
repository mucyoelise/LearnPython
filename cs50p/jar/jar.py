# Define the Jar class to simulate a cookie jar with a capacity and current cookie count.
class Jar:
    # Initialize the Jar with a default capacity of 12 (or a specified capacity).
    # If the capacity is negative, raise a ValueError.
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Not a non negative int')
        self.capacity = capacity  # Set the capacity.
        self.cookies = 0  # Initialize the number of cookies in the jar to 0.

    # Define a string representation for the jar, displaying cookies as 🍪 symbols.
    def __str__(self):
        return f"{self.cookies * '🍪'}"  # Return a string showing the cookies in the jar.

    # Method to deposit cookies into the jar.
    # It checks if adding cookies exceeds the jar's capacity.
    def deposit(self, n):
        curr_cookies = self.cookies + n  # Calculate the new number of cookies.
        if curr_cookies > self._capacity:  # If the new cookie count exceeds capacity, raise an error.
            raise ValueError('Exceeds the capacity')
        self.cookies = curr_cookies  # Update the number of cookies in the jar.

    # Method to withdraw cookies from the jar.
    # It checks if withdrawing cookies results in a negative number of cookies.
    def withdraw(self, n):
        curr_cookies = self.cookies - n  # Calculate the new number of cookies.
        if curr_cookies < 0:  # If the number of cookies would be negative, raise an error.
            raise ValueError('Exhausted all the self.cookies')
        self.cookies = curr_cookies  # Update the number of cookies in the jar.

    # Getter for the capacity of the jar.
    @property
    def capacity(self):
        return self._capacity  # Return the current capacity of the jar.
    
    # Setter for the capacity of the jar. It ensures the capacity can't be set to a negative value.
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError("Capacity can't be negative number")  # Raise an error for negative values.
        self._capacity = n  # Set the new capacity.

    # Property for the current number of cookies in the jar.
    @property
    def size(self):
        return self.cookies  # Return the current number of cookies.

# Main function to test the Jar class functionality.
def main():
    coo = Jar(5)  # Create a Jar instance with a capacity of 5.
    coo.deposit(3)  # Deposit 3 cookies into the jar.
    coo.deposit(2)  # Deposit 2 more cookies into the jar.
    coo.withdraw(4)  # Withdraw 4 cookies from the jar.
    coo.capacity = -10  # Try to set a negative capacity (raises an error).
    print(coo)  # Print the string representation of the jar.
    print(coo.capacity)  # Print the current capacity of the jar.

# Ensure the main function is executed if this script is run directly.
if __name__ == "__main__":
    main()
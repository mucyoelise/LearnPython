import math

# ------------------ Defining a class to perform rational numbers operations ---------------
class rat_nbr:
    def __init__(self, numerator, denominator):
        # Constructor to initialize a rational number with a numerator and denominator
        self.numerator = numerator
        self.denominator = denominator

    def simply_output(self):
        # Simplifies the rational number by dividing both the numerator and denominator
        # by their greatest common divisor (GCD).
        gcd_value = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value

    def __sub__(self, other):
        # Subtracts two rational numbers (if the other object is also of type rat_nbr)
        if isinstance(other, rat_nbr):
            # Compute the new numerator and denominator for the subtraction
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            # Create a new rational number object with the computed values
            result = rat_nbr(new_numerator, new_denominator)
            # Simplify the result and return the result
            result.simply_output()
            return result
        # Raise an error if the other operand is not a rat_nbr object
        raise TypeError('The provided value is not type rat_nbr')

    def __add__(self, other):
        # Adds two rational numbers (if the other object is also of type rat_nbr)
        if isinstance(other, rat_nbr):
            # Compute the new numerator and denominator for the addition
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            # Create a new rational number object with the computed values
            result = rat_nbr(new_numerator, new_denominator)
            # Simplify the result and return the result
            result.simply_output()
            return result
        # Raise an error if the other operand is not a rat_nbr object
        raise TypeError('The provided value is not type rat_nbr')

    def __repr__(self):
        # String representation of the rational number object in the format "numerator/denominator"
        return f'{self.numerator}/{self.denominator}'
    
# ------------------- End of defining a class named rat_nbr ------------------------------
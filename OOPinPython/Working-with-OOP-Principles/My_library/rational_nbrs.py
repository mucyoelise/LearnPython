import math

# ------------------ Defining a class to perform rational nbrs operations ---------------
class rat_nbr:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def simply_output(self):
        gcd_value = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd_value
        self.denominator //= gcd_value
    
    def __sub__(self, other):
        if isinstance(other, rat_nbr):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            result = rat_nbr(new_numerator, new_denominator)
            result.simply_output()
            return result
        raise TypeError('The provided value is not type rat_nbr')

        
    def __add__ (self, other):
        if isinstance(other, rat_nbr):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            result = rat_nbr(new_numerator, new_denominator)
            result.simply_output()
            return result
        raise TypeError('The provided value is not type rat_nbr')

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'
    
# ------------------- End of defining a class named rat_nbr ------------------------------
class Item:
    # Class-level attribute: applies a 20% discount on the price
    pay_rate = 0.80 

    # Class-level attribute: stores all instances of Item
    all_instance = []

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Constructor for initializing an Item object
        # It checks if the input types are correct (name should be string, price should be int/float, quantity should be int)
        if not isinstance(name, str):
            raise ValueError(f'Oops! The name value = {name}, must be a string type')
        elif not isinstance(price, (int, float)):
            raise ValueError(f'Oops! The price value = {price}, must be an integer or float type')
        elif not isinstance(quantity, int):
            raise ValueError(f'Oops! The quantity value = {quantity}, must be an integer type')

        # Private attributes for encapsulation (cannot be accessed directly)
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Adding this instance to the class-level list of instances
        Item.all_instance.append(self)

    '''
    Applying the concept of encapsulation to restrict the user from modifying attributes
    once created. Allow modification only when the entered value characters are less than 10.
    This feature is created below using @property and @name.setter decorators.
    '''
    @property
    def name(self):
        # Getter for the name attribute
        return self.__name

    @name.setter
    def name(self, value):
        # Setter for the name attribute: ensures the name is less than 10 characters
        if len(value) > 10:
            raise Exception('The name is too long! It should contain at least less than 10 characters')
        else:
            self.__name = value

    '''
    Applying the concept of encapsulation to prevent direct modification of the price attribute.
    Price can only be modified through specific methods like apply_increment() and apply_discount().
    '''
    @property
    def price(self):
        # Getter for the price attribute
        return self.__price

    def apply_discount(self):
        # Applies a discount to the price based on the pay_rate (class-level attribute)
        self.__price = self.__price * self.pay_rate
        return self.__price

    def apply_increment(self, increment_value):
        # Applies an increment to the price based on a given increment percentage
        # Ensures the increment_value is a positive number of type int or float
        if not isinstance(increment_value, (int, float)) or increment_value < 0:
            raise ValueError(f'The entered value = {increment_value} is not allowed.\nEnsure it is either int or float type and greater or equal to 0')
        
        # Updates the price by adding the increment percentage to the existing price
        self.__price = self.__price + (self.__price * increment_value)
        return self.__price

    def totPriceInTheStore(self):
        # Returns the total price of all items in the store based on quantity and price
        return self.price * self.quantity

    def __repr__(self):
        # Provides a string representation of the Item object (for display purposes)
        return f'{self.name}, {self.price}, {self.quantity}'


class Phone(Item):
    # Subclass Phone inherits from Item and adds a feature to track broken phones
    def __init__(self, name: str, price: float, quantity: int = 0, broken_phones: int = 0):
        # Call the parent constructor to initialize name, price, and quantity
        super().__init__(name, price, quantity)

        # Ensures the broken_phones value is an integer
        if not isinstance(broken_phones, int):
            raise ValueError(f'The entered value = {broken_phones} is not an integer type')
        
        # Initializes the number of broken phones
        self.broken_phones = broken_phones

    def remained_phone(self):
        # Returns the number of phones remaining in the store (after accounting for broken phones)
        return self.quantity - self.broken_phones

    def __repr__(self):
        # Provides a string representation of the Phone object (calls the parent __repr__ method for common attributes)
        return f'{super().__repr__()}, {self.broken_phones}'
# Class definition for modeling an Item with attributes and methods
class Item:
    # Class-level attributes
    pay_rate = 0.80  # Default pay rate applied after a 20% discount (class-level)
    all_instance = []  # List to store all instances of Item created

    def __init__(self, name: str, price: float, quantity: int = 0):
        # Initialize instance-level attributes with checks for proper types
        if not isinstance(name, str):
            raise ValueError(f'Oops! The name value = {name}, must be a string type')
        elif not isinstance(price, (int, float)):
            raise ValueError(f'Oops! The price value = {price}, must be an integer or float type')
        elif not isinstance(quantity, int):
            raise ValueError(f'Oops! The quantity value = {quantity}, must be an integer type')

        # Instance-level attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Appending the instance's dictionary representation to all_instance
        Item.all_instance.append(self.__dict__)

    def totPriceInTheStore(self):
        # Method to calculate total price without discount
        return self.price * self.quantity

    def priceWithDiscount(self):
        # Method to calculate price after applying the class-level discount rate (pay_rate)
        return self.price * self.pay_rate

# Creating instances of the Item class
item1 = Item("iPhone", 100, 4)
item2 = Item("Laptop", 100, 4)
item3 = Item("Lap-cable", 100, 4)
item4 = Item("Phone-cable", 100, 4)
item5 = Item("Touch-pad", 100, 4)
item6 = Item("Tablet", 100, 4)

# Printing the names of all items created by the instances
print('\nItem names in objects created:')
for item in Item.all_instance:
    print(item['name'])

# Applying different discount rates for each instance and printing the price after the discount
# Customizing the pay_rate for each item at the instance level
item1.pay_rate = 0.50  # Set a 50% discount for item1
item2.pay_rate = 0.30  # Set a 30% discount for item2
item3.pay_rate = 0.0   # Set a 0% discount for item3 (free)

# Printing the price after discount for each item
print('\nThe following are the price after applying the discount on each instance:')
print(item1.priceWithDiscount())  # Price of item1 after discount
print(item2.priceWithDiscount())  # Price of item2 after discount
print(item3.priceWithDiscount())  # Price of item3 after discount
print(item4.priceWithDiscount())  # Price of item4 after discount (using default pay_rate of 0.80)
print(item5.priceWithDiscount())  # Price of item5 after discount (using default pay_rate of 0.80)
print(item6.priceWithDiscount())  # Price of item6 after discount (using default pay_rate of 0.80)
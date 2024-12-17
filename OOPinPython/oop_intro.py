'''
Python codes defining the structure of an object using class.
Contains pay_rate and all_instance attributes as class level/method attributes.
Contains name, price and quantity attributes as instance level/method attributes. 
The all_instance attribute is a list contains or the instance created in a single program.

'''


class Item:
    pay_rate = 0.80 # The pay rate after 20% of discount applied
    all_instance = []
    def __init__(self, name:str, price:float, quantity:int = 0):
        if not isinstance(name, str):
            raise ValueError(f'Oops! The name value = {name}, must be a string type')
        elif not isinstance(price, (int, float)):
            raise ValueError(f'Oops! The price value = {price}, must be an integer or float type')
        elif not isinstance(quantity, int):
            raise ValueError(f'Oops! The quantity value = {quantity}, must be an integer type')
        
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_instance.append(self.__dict__)
    def totPriceInTheStore(self):
        return self.price * self.quantity
    def priceWithDiscount(self):
        return self.price * self.pay_rate

item1 = Item("iPhone", 100, 4)
item2 = Item("Laptop", 100, 4)
item3 = Item("Lap-cable", 100, 4)
item4 = Item("Phone-cable", 100, 4)
item5 = Item("Touch-pad", 100, 4)
item6 = Item("Tablet", 100, 4)

# Using for loop to iterate through all the instance in the all_instance list
# so as to print all the names of item created by the objects or instance... 
print('\nItem names in objects created:')
for item in Item.all_instance:
    print(item['name'])

# Applying the discount on each instance and print the total price

item1.pay_rate = 0.50 # initialising pay_rate on instancelevel (item1)
item2.pay_rate = 0.30 # initialising pay_rate on instancelevel (item2)
item3.pay_rate = 0.0 # initialising pay_rate on instancelevel (item3)

print('\nThe following are the price after applying the discount on each instance')
print(item1.priceWithDiscount())
print(item2.priceWithDiscount())
print(item3.priceWithDiscount())
print(item4.priceWithDiscount())
print(item5.priceWithDiscount())
print(item6.priceWithDiscount())


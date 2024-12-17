import csv
#-------------------The start of defining a class in the main function-------------------------
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
    
    '''
    Classmethod is used to define other class attributes related to the class and its function/method 
    has the cls argument as their first argument to contain and access the class attributes. 
    '''
    @classmethod
    def instantiate_from_csvfile(cls):
        with open('read_from_file.csv') as aFile:
            reader = csv.DictReader(aFile)
            item_list = list(reader)
        for item in item_list:
            cls(item['Name'], float(item['Price']), int(item['Quantity']))
    
    '''
    Creating a static method to check if entered number is integer or float type. Note that the static method 
    attributes or methods can be declared outside of class. Therefore, any methods/functions in static method 
    don't have object/instance as their first argument for they are just independent themselves.  
    '''
    @staticmethod
    def isinteger(num):
        try:
            num = float(num)
        except ValueError:
            print(f'Unable to convert this "{num}" to a number!')
            exit()

        if isinstance(num, float):
            return num.is_integer()
        else:
            return True

#----------------------- The end of defining a class in the main function ------------------------------

# Calling instantiate_from_csvfile() function to assign the class attributes to the CSVfile Items' data
Item.instantiate_from_csvfile() 

# Checking if all items have been added to the list of instance in the class efficiently
print(f'\nThere are {len(Item.all_instance)} instance(s) created from the CSVfile.')
for item in Item.all_instance: 
    print(item)

# Checking the number if it's an integer type or a float type depend on the points..

print(f'{Item.isinteger(input("\nEnter a number to check if it's an integer type: "))}')

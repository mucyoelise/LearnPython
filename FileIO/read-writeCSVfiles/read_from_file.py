import csv  # Import the CSV module to handle CSV file operations

#-------------------The start of defining a class in the main function-------------------------
class Item:
    pay_rate = 0.80  # Class variable that represents the discount rate (80% of the original price)
    all_instance = []  # Class variable to keep track of all instances of the Item class

    # Constructor (__init__) to initialize the object with name, price, and quantity
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Validation checks for the types of name, price, and quantity
        if not isinstance(name, str):
            raise ValueError(f'Oops! The name value = {name}, must be a string type')
        elif not isinstance(price, (int, float)):
            raise ValueError(f'Oops! The price value = {price}, must be an integer or float type')
        elif not isinstance(quantity, int):
            raise ValueError(f'Oops! The quantity value = {quantity}, must be an integer type')
        
        # Assign values to instance variables
        self.name = name
        self.price = price
        self.quantity = quantity

        # Add the instance's dictionary (attributes) to the all_instance list
        Item.all_instance.append(self.__dict__)

    # Method to calculate total price in the store (price * quantity)
    def totPriceInTheStore(self):
        return self.price * self.quantity

    # Method to calculate price with discount (using the class variable pay_rate)
    def priceWithDiscount(self):
        return self.price * self.pay_rate

    '''
    Class method that reads item data from a CSV file and instantiates Item objects for each row.
    The classmethod must take 'cls' as its first argument (instead of 'self') to access class attributes.
    '''
    @classmethod
    def instantiate_from_csvfile(cls):
        # Open the CSV file and read its contents
        with open('read_from_file.csv') as aFile:
            reader = csv.DictReader(aFile)  # Use DictReader to read the file as a dictionary
            item_list = list(reader)  # Convert the file reader object to a list of dictionaries
        # Iterate over the list of items and instantiate objects for each entry
        for item in item_list:
            # Call the constructor with data from the CSV (Name, Price, Quantity)
            cls(item['Name'], float(item['Price']), int(item['Quantity']))

    '''
    Static method to check if a given number is an integer (or convertible to integer).
    Static methods don't take 'self' or 'cls' as the first argument, as they are independent of the class state.
    '''
    @staticmethod
    def isinteger(num):
        try:
            num = float(num)  # Try converting the input to a float
        except ValueError:
            print(f'Unable to convert this "{num}" to a number!')  # If it fails, print error and exit
            exit()

        # If the number is a float, check if it's an integer
        if isinstance(num, float):
            return num.is_integer()
        else:
            return True  # If it's already an integer, return True

#----------------------- The end of defining a class in the main function ------------------------------

# Calling instantiate_from_csvfile() function to populate the class with data from the CSV file
Item.instantiate_from_csvfile()

# Checking if all items have been successfully added to the 'all_instance' list
print(f'\nThere are {len(Item.all_instance)} instance(s) created from the CSVfile.')
for item in Item.all_instance: 
    print(item)  # Print the dictionary representation of each Item instance

# Prompt the user to enter a number and check if it's an integer or float type
print(f'{Item.isinteger(input("\nEnter a number to check if it's an integer type: "))}')
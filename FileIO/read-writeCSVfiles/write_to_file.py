import csv  # Import the CSV module to work with CSV files

#------------------------START OF DEFINING CLASS(Item)----------------------------
class Item:
    pay_rate = 0.80  # Class variable for the discount rate (20% discount)
    all_instance = []  # Class variable to store all instances of the Item class

    # Constructor (__init__) to initialize an item object with name, price, and quantity
    def __init__(self, name: str, price: float, quantity: int = 0):
        # Type validation checks for the parameters passed during object instantiation
        if not isinstance(name, str):
            raise ValueError(f'Oops! The name value = {name}, must be a string type')
        elif not isinstance(price, (int, float)):
            raise ValueError(f'Oops! The price value = {price}, must be an integer or float type')
        elif not isinstance(quantity, int):
            raise ValueError(f'Oops! The quantity value = {quantity}, must be an integer type')

        # Assign values to instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Append the instance's attributes to the all_instance list (class-level list)
        Item.all_instance.append(self.__dict__)

    # Method to calculate the total price of the item in the store (price * quantity)
    def totPriceInTheStore(self):
        return self.price * self.quantity

    # Method to calculate the price after applying the discount
    def priceWithDiscount(self):
        return self.price * self.pay_rate

    # Class method to write all item data to a CSV file
    @classmethod
    def write_to_csvfile(cls):
        # Open the CSV file for writing, create a CSV DictWriter object to write dictionaries
        with open('write_to_file.csv', mode='w', newline='') as aFile:
            # Define the field names (column headers) for the CSV file
            writerObj = csv.DictWriter(aFile, fieldnames=['name', 'price', 'quantity'])

            # Write the header row (field names)
            writerObj.writeheader()

            # Write all instances (item data) to the CSV file
            writerObj.writerows(cls.all_instance)

    # Static method that serves as the main function to initiate writing to the CSV file
    @staticmethod
    def main_function():
        try:
            # Call the class method to write data to the CSV file
            Item.write_to_csvfile()

            # Print the number of items written to the CSV file
            print(f'\nThe following {len(Item.all_instance)} items have already been written to the CSV file:\n')

            # Print each item's details from the all_instance list
            for item in Item.all_instance:
                print(item)

        except:
            # Handle any errors that may occur during the process
            print(f'\nSome error occurred while running the write_to_csvfile() method in the class(Item)')
            quit()

#-------------------------- END OF DEFINING CLASS(Item) ----------------------------

# Initializing instances of the Item class
item1 = Item("iPhone", 100, 4)
item2 = Item("Laptop", 100, 4)
item3 = Item("Lap-cable", 100, 4)
item4 = Item('Flat-TV', 13400, 5)

# Note: You can add more items like item5 = Item("Dell-lap", 1400, 4) and see if they are written to the CSV.

# Call the main function from the Item class to execute writing to the CSV file and displaying the result
Item.main_function()

print()  # Print an empty line for clean output formatting
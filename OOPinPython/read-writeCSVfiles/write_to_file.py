import csv

#------------------------START OF DEFINING CLASS(Item)----------------------------
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
    
    @classmethod
    def write_to_csvfile(cls):
        with open('write_to_file.csv', mode='w', newline='') as aFile:
            writerObj = csv.DictWriter(aFile,fieldnames=['name','price','quantity'])
            writerObj.writeheader()
            writerObj.writerows(cls.all_instance)
    @staticmethod
    def main_function():
        try:
            Item.write_to_csvfile()
            print(f'\nThe following {len(Item.all_instance)} items have already written to the CSVfile:\n')
            for item in Item.all_instance:
                print(item)
        except:
            print(f'\nSome error occured while running the write_to_csvfile() method in the class(Item)')
            quit()
#-------------------------- END OF DEFINING CLASS(Item) -----------------------------

'''Initialising our instances to the class named Item'''
item1 = Item("iPhone", 100, 4)
item2 = Item("Laptop", 100, 4)
item3 = Item("Lap-cable", 100, 4)
item4 = Item('Flat-TV', 13400, 5)
'''
Note that you can try adding your own items like [ item5 = Item("Dell-lap", 1400, 4) ],
and run to check if it's added to the file named(write_to_file.csv).
'''

Item.main_function() # Calling the main function of the class Item to check for the output
print()
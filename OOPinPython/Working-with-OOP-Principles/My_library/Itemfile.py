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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        Item.all_instance.append(self)
    '''
    Applying the concept of encapsulation to strict/limit the user from doing some action 
    like modifying attributes once created.Allow modification only when the entered value
    characters is less than 10. This feature is created below @property in @name.setter. 
    '''
    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long! It should contain at least less than 10 characters')
        else:
            self.__name = value
            
    '''Applying the concept of encapsulation by stricting the user to don't modify the object 
    attribute named price once created. You can only modify this through the help of some methods 
    like apply_increment() and apply_discount()'''
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self.__price
    
    def apply_increment(self, increment_value):
        if not isinstance(increment_value, (int,float)) or increment_value < 0:
            raise ValueError(f'The entered value = {increment_value} is not allowed.\nEnsure it is either int or float type and greater or equal to 0')
    
        self.__price = self.__price + (self.__price * increment_value)
        return self.__price
    
    def totPriceInTheStore(self):
        return self.price * self.quantity
    
    def __repr__(self):
        return f'{self.name}, {self.price}, {self.quantity}'

class Phone(Item):
    def __init__(self, name: str, price: float, quantity:int = 0, broken_phones: int = 0):
        super().__init__(name, price, quantity)

        if not isinstance(broken_phones, int):
            raise ValueError(f'The entered value = {broken_phones} is not an integer type')
        
        self.broken_phones = broken_phones
    
    def remained_phone(self):
        return self.quantity - self.broken_phones
    
    def __repr__(self):
        return f'{super().__repr__()}, {self.broken_phones}'
    
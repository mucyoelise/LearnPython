from Itemfile import Item
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
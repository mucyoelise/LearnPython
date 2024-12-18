from My_library import Itemfile

# Trying to modify attribute restricted to read-only named 'price' by
# using object_methods named apply_increment and apply_discount.
item1 = Itemfile.Phone("iPhone-8Pro", 750, 4, 2)

print(f'\n{item1.__class__.__name__}: {item1}')
print('\n-------------------- Data1 -------------------\n')

print(f'Total Price in the store started: {item1.totPriceInTheStore()}')
item1.apply_increment(0.2)
print(f'The price after applying increment: {item1.price}')
item1.apply_discount()
print(f'The price after applying discount: {item1.price}')


#Working with inheritance/child class named Phone to define the property of 
# broken phones. The following codes contain the phone name iPhone-XPro that 
# was initially 3 but unfortunately 2 are broken. 

print('\n-------------------- Data2 -------------------\n')
print(f'There were {item1.quantity} {item1.name} in the store.')
print(f'The broken phones are {item1.broken_phones} with name {item1.name}')
print(f'The remained phone in the store named "{item1.name}": {item1.remained_phone()}')
print()

string = 'Hello Everyone! Today we are going to learn Python....'
print(f'Given string is: {string}')

print(f'Print the whole string: {string[:]}')
print(f'Printing "Hello" only in the string: {string[:6]}')
print(f'Printing "Today we are going" only in the string: {string[16:35]}')

# Or you can use both split and slicing as follow

check_string = string.split()

print(f'Printing "Today we are going" in a list using both slicing and split: {check_string[2:6]}')

print('')




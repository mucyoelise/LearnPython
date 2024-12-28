#--------Assigning dictionary-----------
book = dict()  # Create an empty dictionary called 'book'
book['title'] = 'Red Moon white'  # Add a key 'title' with the value 'Red Moon white'
book['authors'] = 'T.Kayigamba Ognes'  # Add a key 'authors' with the value 'T.Kayigamba Ognes'

# Overwriting the previous values in the dictionary
book['title'] = 'Truth or Dare'  # Change the value of 'title' to 'Truth or Dare'
book['authors'] = 'Kayitare Onyesis'  # Change the value of 'authors' to 'Kayitare Onyesis'

print(book)  # Print the updated dictionary

#---------Other things to do in a dictionary
# Creating a dictionary called 'president' with keys as president names and values as the years they became president
president = {
    'Paul George': 1990,  # 'Paul George' became president in 1990
    'Black Obama': 2000,  # 'Black Obama' became president in 2000
    'Donald Trump': 2010,  # 'Donald Trump' became president in 2010
}

# dictionary does not support indexing; that's why we only access on the key only
# Using a loop to iterate through the dictionary's keys
for prez in president:
    print(f'{prez} was the president of America.')  # Print the president's name

print('Done!!')  # Indicate the loop is done
print()  # Print a blank line

# To print both president and the year; we need to convert 
# this dict to a list of tuple using method .items()

president_list = president.items()  # Convert the dictionary into a list of tuples (key, value) pairs
print(f'Our dictionary before converted: {president}')  # Print the original dictionary
print(f'Our dictionary after converted:  {president_list}')  # Print the dictionary after conversion to a list of tuples
print()  # Print a blank line

# Iterate through the list of tuples to print both the year and president's name
for prez, year in president_list:
    print('In {}, {} was president of America.'.format(year, prez))  # Print the year and the president's name

print('Done!!')  # Indicate the loop is done
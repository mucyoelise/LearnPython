#--------Assigning dictionary-----------
book = dict()
book['title'] = 'Red Moon white'
book['authors'] = 'T.Kayigamba Ognes'
book['title'] = 'Truth or Dare'
book['authors'] = 'Kayitare Onyesis'

print(book)
#---------Other things to do in a dictionary
president = {
    'Paul George': 1990,
    'Black Obama': 2000,
    'Donald Trump': 2010,
}

# dictionary does not support indexing; that's why we only access on the key only

for prez in president:
    print(f'{prez} was the president of America.')

print('Done!!')
print()

# To print both president and the year; we need to convert 
# this dict to a list of tuple using method .items()
president_list = president.items()
print(f'Our dictionary before converted: {president}')
print(f'Our dictionary after converted:  {president_list}')
print()

for prez, year in president_list:
    print('In {}, {} was president of america.'.format(year, prez))

print('Done!!')

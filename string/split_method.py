sentence = input('Enter a string: ')
print(f'Entered string: {sentence}')

spl_sentence = sentence.split(',') 

# split cut the string into pieces depend on entered argument
# and as a result keeps the separated things in a list.
# By default split() method uses space as an argument.

print(f'String after splitted: {spl_sentence}')
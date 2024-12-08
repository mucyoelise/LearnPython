# Tuple need to be initialised once created because
# You can not alter its contents after creation passed

turple_var = ('Harry', 'Kenny', 10, 10, 10, 'Denns') 
print(f'The element of tuple is: {turple_var}')

# -----------Using index() method to check for index of an element--------------- 

print(f'The element stored in index 3 is: {turple_var[3]}')
print(f'The index of element 10 so far is: {turple_var.index(10)}')

#-----------Using count() method to count for a single element occurance-------------

print(f'Our tuple contain {turple_var.count(10)} tens(10)')

#-----------Other way to assign tuples--------------------

(pref_name, tel_number) = ('Harry', '+250790467044')
print(pref_name,':',tel_number)

#------------Comparing two tuples-------------------

a = (123, 1223)  
b = (132, 234)
if a > b :
    print('Tuple a is max')
elif a == b :
    print('Tuples are equal')
else:
    print('Tuple b is max')
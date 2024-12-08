var_list = list()
#-------------USING APPEND TO GIVE LIST SOME ELEMENTS------------------

for _ in range(5):
    var_list.append(int(input('Enter 5 numbers in the list: ')))
print(f'\nEntered numbers are: {var_list}')

#-----------Finding the sum and average of entered number in a list:-----------

average = sum(var_list)/len(var_list)
print(f'Average is: {average}')

# --------------------Reversing the list------------------------------
var_list.reverse() # This will change the var_list to the new version of reversed list

print(f'The list reversed: {var_list}')

# --------------------Poping in the list-------------------------------
var_list.pop() 

# Note that pop can take an index of element to remove in the list. If not 
# pop() method removes the last element into the list. It uses stack(LIFO)

print(f'Using popping into the list: {var_list}')

# ------------------ Remove method in the list-------------------------
value = int(input('Enter an element to remove in the list so far: '))
var_list.remove(value) 

# Note that it must to give remove() method argument 
# as the element to delete in the list not its index

print(f'\nUsing removing method: {var_list}')

#----------------INSERTING INTO THE LIST SO FAR-----------------------

var_list.insert(1,56) # insert method takes two arguments(index, value-to-insert)

print(f'Inserting 56 into the list index 1: {var_list}')
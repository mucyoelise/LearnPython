# Create an empty list to hold the entered numbers
var_list = list()

#-------------USING APPEND TO GIVE LIST SOME ELEMENTS------------------

# Loop to take 5 numbers as input from the user and append them to the list
for _ in range(5):
    var_list.append(int(input('Enter 5 numbers in the list: ')))

# Print the list after all elements have been entered
print(f'\nEntered numbers are: {var_list}')

#-----------Finding the sum and average of entered number in a list:-----------

# Calculate the average of the numbers in the list
average = sum(var_list) / len(var_list)

# Print the calculated average
print(f'Average is: {average}')

# --------------------Reversing the list------------------------------
# Reverse the list in-place using the reverse() method
var_list.reverse()  # This will change the var_list to the new version of the reversed list

# Print the list after it has been reversed
print(f'The list reversed: {var_list}')

# --------------------Poping in the list-------------------------------
# Pop the last element from the list (default behavior of pop() without an index)
var_list.pop() 

# Print the list after popping the last element
print(f'Using popping into the list: {var_list}')

# ------------------ Remove method in the list-------------------------
# Take an element as input from the user to remove from the list
value = int(input('Enter an element to remove in the list so far: '))

# Remove the first occurrence of the entered element from the list
var_list.remove(value)

# Print the list after the element has been removed
print(f'\nUsing removing method: {var_list}')

#----------------INSERTING INTO THE LIST SO FAR-----------------------
# Insert the number 56 at index 1 of the list
var_list.insert(1, 56)  # insert method takes two arguments (index, value-to-insert)

# Print the list after inserting the value 56 at index 1
print(f'Inserting 56 into the list index 1: {var_list}')
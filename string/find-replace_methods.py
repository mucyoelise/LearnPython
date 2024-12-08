string = 'If someon tels you that you are his friend; just appreciate!'
print(f'Given this string: {string}')

# -------REPLACE METHOD IN STRING---------------:

updating_someone = string.replace('someon', 'someone')
print(f'\nUpdating someon to someone in the string: {updating_someone}')

updating_all = updating_someone.replace('tels', 'tells')
print(f'\nUpdating tels to tells in the string so far: {updating_all}')

# -------FIND METHOD IN STRING (Searching)-----------:

find_someone = updating_all.find('someone')
# Note that find_someone is going to contain index of s = 3
print(f'\nSearching for "first-s" in the string position: {find_someone}')
print('')
# -------USE ALL THE METHODS SO FAR-----------:

new_string = '      If someone tells you that you are his friend; just appreciate!     '
print(f'Given new string: {new_string}')

# Clearing all those white-spaces in the new_string using strip method:

clear_whtspace = new_string.strip()
print(f'Removing the white space in the string: {clear_whtspace}')

# ------------Editing friend to best friend in the string-------------

updated_string = clear_whtspace.replace('friend','bestfriend')

print(f'Updating the new string friend to bestfriend: {updated_string}')

print('')


from My_library import rational_nbrs

''' Note that you can try changing arguments in rat_nbr(numerator, denomerator) to check if it works!'''

num1 = rational_nbrs.rat_nbr(2, 6) # Initialising num1 to be a rational nbr type with value 2/6
num2 = rational_nbrs.rat_nbr(2,3) # Initialising num2 to be a rational nbr type with value 2/3
num3 = rational_nbrs.rat_nbr(3,7) # Initialising num3 to be a rational nbr type with value 3/7

sum = num1+num2+num3 # Calculating sum of those 3 variables: num1, num2, and num3
diff = num1-num2-num3 # Calculating difference of those 3 variables given.

print(f'Sum of rational numbers given is: {sum} and its difference is: {diff}')
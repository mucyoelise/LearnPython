#-----------Writing into the file using WITH operator to open the file----------------

import csv  # Import the CSV module to work with CSV files

# Open the 'Book1.csv' file in append mode ('a')
with open('Book1.csv', 'a') as file:
    # Create a CSV writer object
    lines = csv.writer(file)
    
    # Write a new row to the CSV file with the values ['Jane', '0792347238']
    lines.writerow(['Jane', '0792347238'])
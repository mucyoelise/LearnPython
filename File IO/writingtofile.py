#-----------Writing into the file using WITH operator to open the file----------------

import csv

with open('Book1.csv', 'a') as file:
    lines = csv.writer(file)
    lines.writerow(['Jane', '0792347238'])


#-----------Reading the file using WITH operator to open the file----------------
file_list = []
with open('Book1.csv') as file:
    for line in file:
        print(line.strip())
        names, telephone = line.split(',')
        file_list.append((names,telephone.strip()))
print('\n------------Reading file into the list of tuples:--------------------')
print(f'\n{file_list}')
print()


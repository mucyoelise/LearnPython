from tabulate import tabulate
import sys
import csv

def main():
    data_list = getfile_file_data()
    well_format = tabulate(tabular_data=data_list,headers='keys',tablefmt='grid')
    print(well_format)

def getfile_file_data():
    if len(sys.argv) > 2 :
        sys.exit('Too may arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few arguments')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        row_list = list()
        try:
            with open(sys.argv[1]) as aFile:
                reader = csv.DictReader(aFile)
                for line in reader:
                    row_list.append(line)
        except FileNotFoundError:
            sys.exit('File does not exist')
    return row_list

if __name__ == '__main__':
    main()
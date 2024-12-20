import sys
import csv

def main():
    new_data = []
    old_data = read_file()
    for dictionary in old_data:
        name1,name2 = dictionary['name'].split(',')
        new_data.append({'last': name1.lstrip(), 'first': name2.lstrip(), 'house': dictionary['house']})
    
    write_file(new_data)

def read_file():
    if len(sys.argv) > 3:
        sys.exit('Too many arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few arguments')
    
    for files in sys.argv[1:]:
        if not '.csv' in files:
            sys.exit(f'{files} is not a CSV file')
    try:
        lines_list = list()
        with open(sys.argv[1]) as aFile:
            reader = csv.DictReader(aFile)
            for lines in reader:
                lines_list.append(lines)
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
    return lines_list

def write_file(dict_list):

    with open(sys.argv[2],'w') as aFile:
        writer = csv.DictWriter(aFile, fieldnames=['first', 'last', 'house'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(dict_list)

if __name__ == '__main__':
    main()
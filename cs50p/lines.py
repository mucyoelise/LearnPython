import sys

def main():
    count_lines = 0
    pyfile = valid_file()

    try:
        with open(pyfile) as aFile:
            row_list = aFile.readlines()
            for row in row_list:
                row = row.strip().replace('\n','')
                if not row.startswith("#") and not row == '':
                    count_lines += 1
    except FileNotFoundError:
        sys.exit('File does not exist')
    print('Number of lines:', count_lines)

def valid_file():
    if len(sys.argv)< 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv)>2:
        sys.exit('Too many command-line arguments')
    else:
        if not sys.argv[1].endswith('.py'):
            sys.exit('Not a Python file')
        return sys.argv[1] 

if __name__ == '__main__':
    main()
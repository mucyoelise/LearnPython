def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s:str):

    if not 2 <= len(s) <= 6 or not s.isupper():
        return False

    for i, char in enumerate(s):
        try:
            int(char)
            if i < 2 or char == '0':
                return False

            else:
                nbrInd = s.find(char)
                return is_nbr_btn(nbrInd, s)
        except:
            if i == len(s) - 1:
                return True
            pass

def is_nbr_btn(index:int, string:str):

    numbers = string[index:]

    try:
        int(numbers)
        return True
    except:
        return False

if __name__ == '__main__':
    main()
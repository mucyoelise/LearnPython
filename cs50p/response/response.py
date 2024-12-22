import validator_collection

def main():

    print(validate_email(input("What's your email address? ")))

def validate_email(s:str):

    return 'Valid' if validator_collection.is_email(s) else 'Invalid'

if __name__ == '__main__':
    main()
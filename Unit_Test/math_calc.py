def main():
    try:
        num = int(input('Enter a number: '))
    except ValueError:
        print(f'Fatal: "{num}" ~ The value entered is not a number.')
        exit(1)
    
    print(f"{num} squared is: {square(num)}")

def square(num):
    return num ** 2

if __name__ == "__main__":
    main()
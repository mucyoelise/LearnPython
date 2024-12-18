def main():
    name = input('Enter your name: ')
    print(greet(name))

def greet(name = 'world'):
    return f"Hello, {name}!"

if __name__ == "__main__":
    main()
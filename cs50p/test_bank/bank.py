def main():
    greet = input('Greeting: ').strip()
    print(f"${value(greet)}")

def value(greeting):
    if not greeting.lower().startswith('hello') and greeting.lower().startswith('h'):
        return 20
    elif not greeting.lower().startswith('hello') and not greeting.lower().startswith('h'):
        return 100
    else:
        return 0

if __name__ == "__main__":
    main()
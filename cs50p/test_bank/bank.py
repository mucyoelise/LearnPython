def main():
    # Prompt for the greeting input and strip leading/trailing spaces
    greet = input('Greeting: ').strip()

    # Call the value function to get the corresponding value for the greeting and print it
    print(f"${value(greet)}")

def value(greeting):
    # Convert the greeting to lowercase to handle case-insensitivity

    # Check if the greeting starts with "hello" or "h"
    if greeting.lower().startswith("hello"):
        return 0  # If it starts with "hello", the value is 0
    elif greeting.lower().startswith("h"):
        return 20  # If it starts with "h", but not "hello", the value is 20
    else:
        return 100  # If it doesn't start with "hello" or "h", the value is 100

# Entry point of the program
if __name__ == "__main__":
    main()
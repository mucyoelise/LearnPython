import re  # Import the regular expression module to match the IP address pattern.

# Main function to interact with the user.
def main():
    # Prompt the user for an IPv4 address input and strip any leading/trailing whitespace.
    print(validate(input("IPv4 Address: ").strip()))

# Function to validate the given IPv4 address.
def validate(ip):
    # Regular expression to match a pattern of four numeric parts separated by dots (e.g., "192.168.1.1").
    if match := re.search(r'^(.+)\.(.+)\.(.+)\.(.+)$', ip):
        # Extract the four parts of the IP address.
        part1 = match.group(1)
        part2 = match.group(2)
        part3 = match.group(3)
        part4 = match.group(4)
    else:
        return False  # Return False if the IP address does not match the pattern.

    try:
        # Check each part to ensure it's a valid number between 0 and 255.
        for part in [part1, part2, part3, part4]:
            # Convert each part to an integer and check if it lies between 0 and 255.
            if not 255 >= int(part) >= 0:
                return False  # Return False if any part is out of the valid range.
        return True  # Return True if all parts are valid.
    except ValueError:
        # Catch ValueError in case any part cannot be converted to an integer (e.g., non-numeric characters).
        return False

# Entry point to run the program when executed as a script.
if __name__ == "__main__":
    main()
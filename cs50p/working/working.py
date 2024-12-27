import re  # Importing regular expressions (re) module to work with string patterns

def main():
    # Main function to get input from the user and process the time conversion.
    print(convert(input("Hours: ")))  # Prompt the user for the time range and print the converted result

def convert(s: str):
    # This function takes a string `s` representing a time range in 12-hour format and converts it to 24-hour format.
    
    # Regular expression to match input in the format '9:00 AM to 5:00 PM' or similar
    if match := re.search(r'^([0-9]+(?::[0-9]+)?) (AM|PM) to ([0-9]+(?::[0-9]+)?) (AM|PM)$', s):
        # If the input matches the expected 12-hour time format, extract start and end times.
        start_time = match.group(1)  # Extract the start time (e.g., '9:00')
        end_time = match.group(3)    # Extract the end time (e.g., '5:00')
    else:
        # If the input doesn't match the expected format, raise a ValueError.
        raise ValueError('Not in the 12-Hour Format')

    # Check if start_time has minutes (i.e., contains ':') and call the appropriate function to handle conversion
    if ':' in start_time:
        start_time = hourWithMin(start_time, match.group(2))  # Call function to convert start time with minutes
    else:
        start_time = hourOnly(start_time, match.group(2))  # Call function to convert start time without minutes
    
    # Check if end_time has minutes and call the appropriate function to handle conversion
    if ':' in end_time:
        end_time = hourWithMin(end_time, match.group(4))  # Call function to convert end time with minutes
    else:
        end_time = hourOnly(end_time, match.group(4))  # Call function to convert end time without minutes
    
    # Return the formatted time range in 24-hour format.
    return f'{start_time} to {end_time}'    

def hourWithMin(time: str, merid: str):
    # This function converts a time string with hours and minutes from 12-hour format to 24-hour format.
    
    hour, min = time.split(':')  # Split the time into hour and minute
    hour_float, min_float = float(hour), float(min)  # Convert both hour and minute to floats for validation
    
    # Check if hour and minute are valid integers.
    if not hour_float.is_integer() or not min_float.is_integer():
        raise ValueError('Specified number has floats')  # If not integers, raise an error

    # Validate the ranges for hour (0-23) and minute (0-59)
    if not 0 <= int(min) < 60 or not 0 < int(hour) < 24:
        raise ValueError('Either minutes or hour out of range')  # Raise error if values are out of range

    # If time is in 'AM' period
    if merid == 'AM':
        if int(hour) == 12:
            # Convert '12 AM' to '00:00' for midnight
            return f'00:{min}'
        else:
            # For other AM times, format to 'HH:mm' (adding leading zero if needed)
            return f'0{hour}:{min}' if int(hour) < 10 else f'{hour}:{min}'
    
    # If time is in 'PM' period
    else:
        if int(hour) == 12:
            # '12 PM' should stay as '12:00' for noon
            return f'{hour}:{min}'
        else:
            # Convert PM times by adding 12 hours to the hour
            return f'{int(hour) + 12}:{min}'

def hourOnly(hour: str, merid: str):
    # This function handles times with only the hour (e.g., '9 AM' or '12 PM').
    
    hour_float = float(hour)  # Convert the hour to float for validation
    min = f'00'  # If no minutes are provided, assume '00' for minutes
    
    # Validate that hour is an integer
    if not hour_float.is_integer():
        raise ValueError('Hour has floats nbr')  # Raise error if hour is a float

    # Check if hour is in valid range (1-12)
    if 0 >= int(hour) >= 12:
        raise ValueError('Hour is outOfRange')  # Raise error if hour is out of range
    
    # For 'AM' period
    if merid == 'AM':
        if int(hour) == 12:
            # Convert '12 AM' to '00:00' (midnight)
            return f'00:{min}'
        else:
            # For other AM hours, format to 'HH:00' (adding leading zero if needed)
            return f'0{hour}:{min}' if int(hour) < 10 else f'{hour}:{min}'
    
    # For 'PM' period
    else:
        if int(hour) == 12:
            # '12 PM' remains '12:00'
            return f'{hour}:{min}'
        else:
            # For other PM hours, add 12 to the hour (convert to 24-hour format)
            return f'{int(hour) + 12}:{min}'

if __name__ == "__main__":
    # Entry point of the program, which invokes the main function
    main()
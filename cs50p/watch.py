import re  # Importing the regular expressions module for pattern matching

def main():
    """
    Main function to prompt the user for HTML input and print the parsed YouTube URL.
    """
    print(parse(input("HTML: ")))  # Get the HTML input and parse the YouTube URL

def parse(s: str):
    """
    Extracts and parses a YouTube URL from the provided HTML string.
    """
    # Split the HTML string into attributes based on spaces
    attr_list = s.split(' ')
    
    # Iterate through the attributes to find the 'src' attribute
    for attr in attr_list:
        if attr.startswith('src'):  # Look for attributes that start with 'src'
            # Use a regex pattern to find a YouTube URL in double quotes
            if url := re.search(r'("https?://(?:www\.)?youtube\.com/.+")', attr):
                return format_url(url.group(1))  # Format and return the extracted URL
            return None  # Return None if no valid URL is found

def format_url(url: str):
    """
    Converts a full YouTube URL to its shortened equivalent.
    """
    # Remove unnecessary characters and format the URL as youtu.be
    url = url.replace('"', '').replace('youtube.com', 'youtu.be')
    url = url.replace('http:', 'https:').replace('/embed', '').replace('www.', '')
    return url  # Return the shortened YouTube URL

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly

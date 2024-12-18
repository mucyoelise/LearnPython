import re

# get the url from twitter
url = input('Twitter URL: ').strip()

# Checking the url and extract the username from it
if matches := re.search(r"^(?:https?)?(?:://)?(?:www\.)?(?:twitter|x)\.com/(\w+)", url, re.IGNORECASE):
    print(f'Username: {matches.group(1)}')

else: print("Can't access the username!")
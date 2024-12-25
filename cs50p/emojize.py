import emoji  # Importing the emoji module to add emojis to the output

# Prompt the user to enter their name and capitalize the first letter
user_input = input('\nEnter your name: ').capitalize()

# Define the emojis using the emojize function with alias names
heart_emoji = emoji.emojize(':red_heart:', language='alias')  # Red heart emoji
cry_emoji = emoji.emojize(':sob:', language='alias')  # Crying emoji

# Print a personalized message including the user's name and the emojis
print(f'Hello {user_input}, I{heart_emoji} you!{cry_emoji}\n')
import emoji

user_input = input('\nEnter your name: ').capitalize()
heart_emoji = emoji.emojize(':red_heart:', language='alias')
cry_emoji = emoji.emojize(':sob:', language='alias')

print(f'Hello {user_input}, i{heart_emoji}  you!{cry_emoji}\n')
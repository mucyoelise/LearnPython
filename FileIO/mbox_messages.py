name = input('Enter file name: ')
emails_list = list()
try:
    file = open(name)
except:
    print("File can't open, check and try again later!")
    exit()
for line in file:
    if line.startswith('From '):
        email = line.split()[1]
        emails_list.append(email)
file.close()
data_dict = {email:emails_list.count(email) for email in emails_list}
for email, occurance in data_dict.items():
    if occurance == max(data_dict.values()):
        print(f'An email sends the greatest number of mail message is: {email} with {occurance} messages.')

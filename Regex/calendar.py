import re

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def comma_valid_format(mon, dy, yr):
    try:

        if not mon in month_list or not len(yr) == 4 or not int(dy) <= 30:
            print('Oops!!: Year should have 4 digits; (jan-Dec) for months and not more than 30 for Days')
            return False

        return True
    except ValueError:
        return False


def slash_valid_format(mon, dy, yr):
    try:
        if not len(yr) == 4 or not int(mon) <= 12 or not int(dy) <= 30:
            print('Oops!!: Year should have 4 digits; not more than 12 for months and not more than 30 for Days')
            return False

        int(yr)
        return True
    except ValueError:
        return False


def get_input():
    while True:
        user_input = input('Date: ').strip().capitalize()

        if '/' in user_input:
            if re.search(r'^[0-9]+/[0-9]+/[0-9]+$', user_input):
                month, day, year = user_input.split('/')

                if slash_valid_format(month, day, year):
                    if int(month) <= 9:
                        month = '0'+month
                    if int(day) <= 9:
                        day = '0'+day
                    return f'{year}-{month}-{day}'
                else: continue
            else:
                raise ValueError('Oops! Not in the real format\nExpected: month/day/year')
        elif ',' in user_input:
            if re.search(r'^.+ .+, .+$', user_input):
                month_day, year = user_input.split(',')
                year = year.strip()
                month, day = month_day.split()
                if comma_valid_format(month, day, year):
                    month = month_list.index(month) + 1
                    if int(month) <= 9:
                        month = '0' + str(month)
                    if int(day) <= 9:
                        day = '0' + day
                    return f'{year}-{month}-{day}'
                else: continue
            else:
                raise ValueError('Oops! Not in the real format\nExpected: month day, year')

        else:
            print(f'Oops!! "{user_input}" not in the middle-endian order.\nexpected: (month/day/year or month_name day, year)')

print(get_input())
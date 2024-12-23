import sys
from datetime import date
from inflect import engine

class TimeCalc():
    def __init__(self, date):
        self.date = date

    def __sub__(self, other):
        return  f'{self.date - other.date}'

    def __repr__(self):
        output = engine().number_to_words(num=self.date, andword='')
        return f'{output.capitalize()} minutes'

def main():

    today = TimeCalc(date.today())

    try:
        input_date = date.fromisoformat(input('Date of Birth: '))
        dob = TimeCalc(date = input_date)

    except ValueError:
        sys.exit(f'Invalid input')

    user_days = today - dob

    user_days_part = user_days.split(',')[0]
    user_days_int = int(user_days_part.split()[0])

    user_min_int= user_days_int * 24 * 60
    user_min_word = TimeCalc(user_min_int)

    print(user_min_word)

if __name__ == '__main__':
    main()

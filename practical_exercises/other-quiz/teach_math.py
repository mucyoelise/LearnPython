from random import randint

## ---------------- The following is the main function of the whole program -----------------

def main_function(): 
    user_level = get_level()
    user_marks = 0
    for _ in range(10):
        x, y = generate_question(user_level)
        trials = 3
        while True:
            if not trials == 0:
                user_answer = get_int(f'\n{x} + {y} = ')
                if x + y == user_answer:
                    user_marks += 1
                    break
                else:
                    trials -= 1
                    print('EEE!')
                    continue
            print('You exhaust your trials for this question; therefore, you lose one mark...')
            print(f'Answer: {x} + {y} = {x + y}')
            break
    print(f'\nYour total marks are: {user_marks}/10')

##--------------------------- Other functions ---------------------------

def get_int(string):
    try:
        return int(input(string))
    except ValueError:
        print('Oops.... you entered a non-number!')
        pass

def get_level():
    while True:
        level = get_int('\nEnter your level: ')
        if level in [1,2,3]:
            return level
        print('Level must be 1, 2, or 3')

def generate_question(n):
    lower_limit = 10*(n - 1)
    upper_limit = (10**n) - 1
    return randint(lower_limit, upper_limit), randint(lower_limit, upper_limit)

if __name__ == '__main__':
    main_function()

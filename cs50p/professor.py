import random

def main():
    level = get_level()
    user_marks = 0
    for questions in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for i in range(4):
            if not i == 3:
                print(f'{x} + {y} = ', end=" ")
                if x + y == get_answer():
                    user_marks += 1 
                    break
                else: 
                    print('EEE') 
                    continue
            print(f'{x} + {y} = {x+y}')
    
    print(f'Score: {user_marks}')
    
def get_level():
    while True:
        try:
            user_level = int(input('Level: '))
            if user_level in (1,2,3):
                return user_level
        except ValueError:
            pass

def generate_integer(user_level):
    low_nbr = 10*(user_level-1)
    high_nbr = (10**user_level)-1
    return random.randint(low_nbr,high_nbr)
    
def get_answer():
    try:
        return int(input())
    except:
        pass


if __name__ == "__main__":
    main()
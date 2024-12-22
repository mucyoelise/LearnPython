import re

def main():
    print(convert(input("Hours: ")))

def convert(s:str):
    if match:= re.search(r'^([0-9]+(?::[0-9]+)?) (AM|PM) to ([0-9]+(?::[0-9]+)?) (AM|PM)$',s):
        start_time = match.group(1)
        end_time = match.group(3)
    else: raise ValueError('Not in the 12-Hour Format')

    if ':' in start_time:
        start_time =  hourWithMin(start_time,match.group(2))
    else: start_time =  hourOnly(start_time,match.group(2))
    
    if ':' in end_time:
        end_time = hourWithMin(end_time,match.group(4))
    else: end_time = hourOnly(end_time,match.group(4))
    
    return f'{start_time} to {end_time}'    

def hourWithMin(time:str,merid:str):
    hour,min = time.split(':')
    hour_float, min_float = float(hour), float(min)
    if not hour_float.is_integer() or not min_float.is_integer():
        raise ValueError('Specified number has floats')
    if not 0<=int(min)<60 or not 0<int(hour)<24:
        raise ValueError('Either minutes or hour out of range')
    if merid == 'AM':
        if int(hour) == 12:
            return f'00:{min}'
        else:
            return f'0{hour}:{min}'
    else:
        return f'{int(hour)+12}:{min}' if int(hour) != 12 else f'{hour}:{min}'
        
def hourOnly(hour:str,merid:str):
    hour_float = float(hour)
    min = f'00'
    if not hour_float.is_integer():
        raise ValueError('Hour has floats nbr')
    if 0>=int(hour)>=12:
        raise ValueError('Hour is outOfRange') 
    if merid == 'AM':
        if int(hour) == 12:
            return f'00:{min}'
        else:
            return f'0{hour}:{min}'
    else:
        return f'{int(hour)+12}:{min}' if int(hour) != 12 else f'{hour}:{min}'


if __name__ == "__main__":
    main()
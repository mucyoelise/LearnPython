name_list = list()
format_string=str()
while True:
    try:
        prompt = input('Name: ').capitalize()
        name_list.append(prompt)
    except KeyboardInterrupt:
        print()
        break
while True:
    if len(name_list) == 1:
        for name in name_list: format_string = name
        break
    elif len(name_list) == 2:
        format_string = name_list[0] + ' and ' + name_list[1]
        break
    else: name_list.insert(len(name_list)-1,'and')
    for ind, name in enumerate(name_list):
        if not ind >= name_list.index('and'):
            format_string = format_string + name + ', '
        else:
            format_string = format_string + name + ' '
    break

print(f'Adieu, adieu, to {format_string.strip()}')
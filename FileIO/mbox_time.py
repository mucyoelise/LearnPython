time_list = list()
with open(input('Enter file name: ')) as file:
    for line in file:
        if line.startswith('From '):
            time_list.append(line.split()[len(line.split())-2])
hour_list = sorted([hour.split(':')[0] for hour in time_list ])
hour_dict = {hour: hour_list.count(hour) for hour in hour_list}
for hour, occurance in hour_dict.items():
    print(f'{hour} {occurance}')

#----------------Checking for this following codes (Both do the same)-------------------------
#time_list = list()
#with open(input('Enter file name: ')) as file:
#    for line in file:
#        if line.startswith('From '):
#            time_list.append(line.split()[len(line.split())-2])
#hour_list = [hour.split(':')[0] for hour in time_list ]
#hour_tuple_dict = sorted({hour : hour_list.count(hour) for hour in hour_list}.items())
#for hour, occurance in hour_tuple_dict:
#    print(f'{hour} {occurance}')
#print(dir(tuple()))



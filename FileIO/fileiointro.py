student_file = open('student_info.txt','r')
counter = 1
for line in student_file: 
    print(f'Line {counter}: {line.strip()}') 
    # We used strip() to remove some white spaces like (\n) in the file
    counter+=1
print()
student_file.close()
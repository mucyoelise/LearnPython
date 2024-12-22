import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    if match := re.search(r'^(.+)\.(.+)\.(.+)\.(.+)$',ip):
       part1 = match.group(1)
       part2 = match.group(2)
       part3 = match.group(3)
       part4 = match.group(4) 
    else:
        return False
    
    try:
        for part in [part1,part2,part3,part4]:
            if not 255 >= int(part) >=0:
                return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"}   
    ]

    list_compreh1("This","is","stuff!")
    list_compreh2(students)

def list_compreh1(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

def list_compreh2(s:list):
    gryffindors = [
        stud["name"] for stud in s if stud["house"] == "Gryffindor"
    ]
    print(gryffindors)

main()
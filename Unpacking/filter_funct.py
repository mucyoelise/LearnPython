def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherin"}   
    ]

    list_compreh(students)

def is_gryffindor(s):
    return s["house"] == "Gryffindor"

def list_compreh(s:list):

    gryffindors = filter(is_gryffindor,s)
    # print(gryffindors); note this won't give you the list...
    for gryffindor in sorted(gryffindors, key=lambda x: x["name"]):
        print(gryffindor["name"])
main()
def main():
    yell("This","is","stuff!")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

main()
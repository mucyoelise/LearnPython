def main():
    usemap("This","is","stuff!")

def usemap(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
    
main()
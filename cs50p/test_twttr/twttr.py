def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")

def shorten(word):
    shorten_word = str()
    for char in word :
        if char.lower() not in 'aeuio':
            shorten_word += char 
    return shorten_word
         
      
if __name__ == '__main__':
    main()
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("What's this? ")
people_say = r'''      
    \\
     \\  
      \\ _____
        | . . |
        |_____|
           |
           |
          /|\
         / | \
        /  |  \
           |
          | |
          | |
          | | 
         _| |_
'''
cowsay.draw(this, people_say) # Calling your own created drawing
engine.say(this)
engine.runAndWait()
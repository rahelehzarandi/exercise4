import random

randomnum=random.randrange(0,10)
print(randomnum)
guessnum=int(input("enter your guess: ",))
while randomnum != guessnum:
    if guessnum > randomnum:
        print("too high")
    elif guessnum < randomnum:
        print("too low")
    guessnum=int(input("enter your guess again:",))
print("correct")

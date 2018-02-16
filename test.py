import time

def displayIntro():
    Jump = input('Hello?\n')
    if Jump == "Hi":
        print("Why")
        PlayAgain()
    elif Jump == "?":
        print("What?")
        PlayAgain()
    else:
        displayIntro()

def PlayAgain():
    PlayAgain = input("Play Again? Yes or No?\n")
    if PlayAgain in {"Yes", "Y"}: #This is the same as if PlayAgain == "Yes" or if PlayAgain == "Y"
        displayIntro()
    if PlayAgain in ("No", "N"): #This is just as mentioned above and these are to created different options within the same string.
        print('Bye')


displayIntro()

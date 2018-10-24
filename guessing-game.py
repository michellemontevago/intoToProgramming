def main ():
    print ("PYTHON GUESSING GAME")
main ()

answer = "lion"

def end ():
    print ("If you would like to exit game, type QUIT")

def game ():
    end()
    print("I'm thinking of an animal...") 
    global answer 
    while True:
        guess = input ("Guess the name of the animal: ".lower().strip())
        if guess[0] == "q":
            break
        elif guess == "lion":
            print ("You are correct!")
            opinion = input ("Do you like this animal? Yes or No?:".lower().strip())
            if opinion[0] == "y":
                print ("Me to!")
            elif opinion == "n":
                print ("Sorry to hear that")
            else:
                print("Sorry I didnt get that") 
            break 
        else:
            print ("Please try again")
game() 
    

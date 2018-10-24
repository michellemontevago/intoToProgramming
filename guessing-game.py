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
        if guess == "quit":
            break
        elif guess == "lion":
            print ("You are correct!")
            break 
        else:
            print ("Please try again")
game() 
    

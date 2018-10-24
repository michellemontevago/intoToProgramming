def main ():
    print ("PYTHON GUESSING GAME")
main ()

answer = "lion"
def game ():
    global answer 
    while True:
        print("I'm thinking of an animal...") 
        guess = input ("Guess the name of the animal: ".lower().strip())
        return guess
        if guess == "lion":
            print ("You are correct!")
            break
        else:
            print ("Please try again")
game() 
    

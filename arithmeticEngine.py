# CMPT 120 - Lab 6
# Michelle Montevago
# 10-29-18

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        try:
            num1 = int(input("Enter the first  number: "))
        except:
            print ("Please input an integer.")
            continue
        try: 
            num2 = int(input("Enter the second number: "))
        except:
            print ("Please input an integer.")
            continue 
        cmd = input("What computation do you want to perform? ").lower()
        if cmd == "add":
            result = num1 + num2
        elif cmd == "sub":
             result = num1 - num2
        elif cmd == "mult":
             result = num1 * num2
        elif cmd == "div":
            result = num1 // num2
        elif cmd == "quit":
            break
        else:
            print("Sorry I do not understand" + cmd + ".")
            continue
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()

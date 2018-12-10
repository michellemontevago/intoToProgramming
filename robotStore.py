#Intro To Programming
#Author: Michelle Montevago
#November 29th, 2018


productNames = [ "Ultrasonic range finder"
                 , "Servo motor"
                 , "Servo controller"
                 , "Microcontroller Board"
                 , "Laser range finder"
                 , "Lithium polymer battery"
                 ]
productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
productQuantities = [ 4, 10, 5, 7, 2, 8 ]

class Product:
    def __init__ (self, name, price, quantities):
        self.name= name
        self.price=price
        self.quantities=quantities
    def stock(self, name, quantities):
        for i in range(len(products)):
            if procust[i].name in products[i].quantities
                return True
            return False 
    def cost(self, price, quantities):
        for i in range (len(products)):
            print(products[i].price * products[i].quantities)
        

products=[Product("Ultrasonic range finder", 2.50, 4),
          Product("Servo motor", 14.99, 10),
          Product("Servo controller", 44.95, 5),
          Product("Microcontroller Board", 34.95, 7),
          Product("Laser range finder", 149.99, 2),
          Product("Lithium polymer battery", 8.99, 8)]



def printStock():
    global products
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(products)):
        if products[i].quantities > 0:
            print(str(i)+")",products[i].name, "$", products[i].price)
    print()

def main():
    global products
    cash = float(input("How much money do you have? $"))
    while cash > 0: 
        printStock()

        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break

        prodId = int(vals[0])
        count = int(vals[1])

        if products[prodId].quantities >= count:
            cost()
            stock() 
            if cash >= products[prodId].price * count:
                products[prodId].quantities -= count
                cash -= products[prodId].price * count
                print("You purchased", count, products[prodId].name+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, we are sold out of", products[prodId].name)

main()



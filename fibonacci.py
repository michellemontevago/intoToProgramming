# Author Michelle Montevago
# September 20th, 2018

num = int (input ("Enter a number: "))

first= 0
second= 1

print("\nResponse: ")
print(first,", ",second, end=",")

for i in range (2,num):
    next = first + second
    print (next,end= ",")

    first= second
    second= next 



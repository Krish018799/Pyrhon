import random

y = random.randint(1,50)

c = 0
x = 0
while x!=y:
    x = int(input("Enter guess number=> "))
    c+=1

print("Count = ", c)
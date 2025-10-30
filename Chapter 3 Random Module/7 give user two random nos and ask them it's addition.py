import random

x = random.randint(1,30)
y = random.randint(1,30)

print("No1: ", x, " No2: ", y)

z = int(input("Enter addition of x and y => "))

if (z == x+y):
    print("Right answer")
else:
    print("Wrong answer")
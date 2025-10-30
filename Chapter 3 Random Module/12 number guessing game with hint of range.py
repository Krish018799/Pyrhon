import random

y = random.randint(1,50)
print(y)
x1 = x2 = 1
x = 0
c = 0
while x!=y:
    x = int(input("Enter guess number=> "))
    if x > 50:
        print("Your range is 1 to 50")
    elif x < y:
        x1 = x
        print("Please think greater than this and your range is ", x1, " to ", x2)
    elif y < x < 50:
        x2 = x
        print("Please think less than that now your range is ", x1, " to ", x2)
    elif x == y:
        print("Yes this is right no")
    c+=1

print("Count = ", c)
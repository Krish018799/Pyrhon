import random

y = random.randint(1,50)
print(y)
c = 0
x = 0
while x!=y:
    x = int(input("Enter guess number=> "))
    if x>y:
        print("Please write less than ", x)
    elif x<y:
        print("Please write grater than ", x)
    else:
        print("Yes this is right no")
    c+=1

print("Count = ", c)
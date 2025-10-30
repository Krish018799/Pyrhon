import random

c1 = 0
c2 = 0

for i in range(1,6):
    x = random.randint(1,30)
    y = random.randint(1,30)
    print("No1: ", x, " No2: ", y)
    z = int(input("Enter addition of x and y => "))
    if (z == x+y):
        print("Right answer")
        c1+=1
    else:
        print("Wrong answer")
        c2+=1

print("Total right answer=> ", c1)
print("Total wrong answer=> ", c2)

# 1. choice 1 for add, 2 for sub, 3 for multi loop 1 to 5
# 2.
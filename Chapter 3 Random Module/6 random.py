import random

c1 = 0
c2 = 0

for i in range(1, 11):
    x=random.randint(-10,10)
    if x > 0:
        print("Positive ", x)
        c1+=1
    else:
        print("Negative ", x)
        c2+=1
print("Total positive no => ", c1)
print("Total negative no => ", c2)
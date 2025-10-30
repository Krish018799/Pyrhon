import random

for i in range(1, 11):
    x = random.randint(1, 40)
    if (x%2==0):
        print("No is even ", x)
    else:
        print("No is odd ", x)
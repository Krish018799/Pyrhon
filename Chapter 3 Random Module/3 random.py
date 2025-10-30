import random
total=0
for i in range(1,6):
    x=random.randint(1,40)
    print("No",i," => ",x)
    total=total+x
print("total of all =",total)
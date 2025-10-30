list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
c1 = 0
c2 = 0
for x in list1:
    if x%2 == 0:
        c1+=1
    else:
        c2+=1

print("Even numbers: ", c1)
print("Odd numbers: ", c2)
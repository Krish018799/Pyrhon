list1 = [11, 12, 15, 22, 99, 77, 200, 66, 2]
c = 0
for x in list1:
    if x%3 == 0:
        c = c + x

print("the sum of no dividable by 3 = ", c)
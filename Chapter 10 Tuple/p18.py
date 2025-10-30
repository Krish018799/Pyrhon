t1 = (11, 22, 33)
t2 = (44, 55, 66)

list1 = list(t1)
for x in t2:
    list1.append(x)
t3 = tuple(list1)
print(t3)
list1 = [11, 9, 3, 44, 11, 99, 11, 38, 49, 20]
list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)

print(list2)
list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
list2 = []
length = len(list1)//2
c = 0
for x in list1:
    list2.append(x)
    c+=1
    if c+1 >= length:
        break

print(list2)
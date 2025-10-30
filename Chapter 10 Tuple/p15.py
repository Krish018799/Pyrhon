t1 = (1, 2, 3, 4)
list1=list(t1)
list2 = []
for x in list1:
    list2.append(x*2)
t1 = tuple(list2)
print(t1)

# method 2
# t1 = tuple(x*2 for x in t1)
# print(t1)
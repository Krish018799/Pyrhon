list1 = [11, 44, 500, 22]
list2 = [11, -44, 500, 22]
c1 = 0
c2 = 0
for x in list1:
    if x > 0:
        c1+=1

for y in list2:
    if y > 0:
        c2+=1

if len(list1) == c1 and len(list2) == c2:
    print("True for both")
elif len(list1) == c1:
    print("True for first and false for second")
elif len(list2) == c2:
    print("True for second and false for first")
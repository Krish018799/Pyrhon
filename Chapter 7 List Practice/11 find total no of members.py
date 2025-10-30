list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

# METHOD 1
c = 0
for x in list1:
    c = c + 1

if c == 0:
    print("The list is empty")

else:
    print("Total no of elements are: ", c)

# METHOD 2:
# print(len(list1))
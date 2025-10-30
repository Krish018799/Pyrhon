list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# if i used to delete position like 0,4,5 then after deleting 0th element the list become short and now total
# total elements are 4 it will indicates the list out of the range bcz of index error

del list1[5]
del list1[4]
del list1[0]

print(list1)

# Other method using slicing
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list2 = list1[1:4]
# print(list2)

# Method 3
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# list1.pop(5)
# list1.pop(4)
# list1.pop(0)
#
# print(list1)
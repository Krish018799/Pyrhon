t1=(11,44,30,55,66,90)
list1=list(t1)
value = 44
if value in list1:
    print("Yes",value,"is in the list")
else:
    print("No",value,"is not in the list")
t1=tuple(list1)
print(t1)
t1 = (11, 22, 33, 44, 55)
value = int(input("Enter value for search: "))
if value in t1:
    print("Yes,",value," is there")
else:
    print("No,", value, " is not there")
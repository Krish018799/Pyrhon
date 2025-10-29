print("Press 1 for square")
print("Press 2 for cube")
op=int(input("Enter opt =>"))

if op==1:
    no=int(input("Enter no =>"))
    print("square = ",no*no)
elif op==2:
    no=int(input("Enter no =>"))
    print("cube = ",no*no*no)
else:
    print("Wrong opt")
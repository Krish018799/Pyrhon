print("Enter 1 for square")
print("Enter 2 for cube\n")

op = int(input("Enter option=> "))

if op == 1:
    no = int(input("Enter no=> \n"))
    print("Square of no=> ", no*no)
elif op == 2:
    no = int(input("Enter no=> \n"))
    print("Cube of no=> ", no*no*no)
else:
    print("Wrong option!")
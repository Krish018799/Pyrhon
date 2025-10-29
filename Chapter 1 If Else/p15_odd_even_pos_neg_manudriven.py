print("Enter 1 for odd even")
print("Enter 2 for positive negetive")

op = int(input("Enter option: "))

if op == 1:
    no = int(input("Enter no: "))
    if no%2 == 0:
        print("no is even")
    else:
        print("no is odd")
elif op == 2:
    no = int(input("Enter no: "))
    if no > 0:
        print("no is positive")
    else:
        print("no is nagetive")
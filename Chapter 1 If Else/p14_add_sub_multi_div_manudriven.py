print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

op = int(input("Enter option: "))

if op == 1:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Add = ", no1 + no2)
elif op == 2:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Sub = ", no1 - no2)
elif op == 3:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Multi = ", no1 * no2)
elif op == 4:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Div = ", no1/no2)
else:
    print("Wrong option")
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")

op = (input("Enter option: "))

if op == "+":
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Add = ", no1 + no2)
elif op == "-":
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Sub = ", no1 - no2)
elif op == "*":
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Multi = ", no1 * no2)
elif op == "/":
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    print("Div = ", no1/no2)
else:
    print("Wrong option")
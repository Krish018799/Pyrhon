b1=b2=b3=b4=0

while True:
    print("Press 1 for Pizza")
    print("Press 2 for Dosa")
    print("Press 3 for Maggi")
    print("Press 4 for Sandwich")

    op = int(input("Enter option=> "))

    if op == 1:
        print("Price = 300")
        qty = int(input("Enter quantity=> "))
        b1 = 300*qty
        print("Total bill = ", b1)
    elif op == 2:
        print("Price = 150")
        qty = int(input("Enter quantity=> "))
        b2 = 150 * qty
        print("Total bill = ", b2)
    elif op == 3:
        print("Price = 90")
        qty = int(input("Enter quantity=> "))
        b3 = 90 * qty
        print("Total bill = ", b3)
    elif op == 4:
        print("Price = 100")
        qty = int(input("Enter quantity=> "))
        b4 = 100 * qty
        print("Total bill = ", b4)
    elif op == 5:
        b = b1 + b2 + b3 + b4
        print("Total bill = ", b)
        print("Bye!")
        break
    else:
        print("Error")
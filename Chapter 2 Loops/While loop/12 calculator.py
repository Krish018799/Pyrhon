while True:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for Exit")

    op = int(input("Enter option=> "))

    if op == 1:
        no1 = int(input("Enter no1=> "))
        no2= int(input("Enter no2=> "))
        print("Addition = ", no1 + no2)
    elif op == 2:
        no1 = int(input("Enter no1=> "))
        no2= int(input("Enter no2=> "))
        print("Subtraction = ", no1 - no2)
    elif op == 3:
        no1 = int(input("Enter no1=> "))
        no2= int(input("Enter no2=> "))
        print("Multiplication = ", no1 * no2)
    elif op == 4:
        no1 = int(input("Enter no1=> "))
        no2= int(input("Enter no2=> "))
        print("Division = ", no1 / no2)
    elif op == 5:
        print("Bye")
        break
    else:
        print("Error")
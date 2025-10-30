while True:
    print("Enter 1 for square")
    print("Enter 2 for cube")
    print("Press 3 for exit")
    op = int(input("Enter option=> "))

    if op == 1:
        no = int(input("Enter no=> "))
        print("Square of no=> ", no * no)
    elif op == 2:
        no = int(input("Enter no=> "))
        print("Cube of no=> ", no * no * no)
    elif op == 3:
        print("Bye")
        break
    else:
        print("Error")
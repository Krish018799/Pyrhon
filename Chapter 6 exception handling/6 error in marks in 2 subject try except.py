try:
    eng = int(input("Enter marks in English => "))
    hindi = int(input("Enter marks in Hindi => "))

    if eng < 0:
        raise ValueError("Why did you enter negative marks in English?")
    elif hindi < 0:
        raise ValueError("Why did you enter negative marks in Hindi?")
    else:
        print("Total marks of two subjects => ", eng + hindi)

except ValueError as e:
    print(e)
except:
    print("Error")
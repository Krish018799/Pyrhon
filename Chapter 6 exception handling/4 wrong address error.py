try:
    address = input("Enter ur string => ")
    if len(address)<5:
        raise ValueError("Why u enter small address")
    else:
        print("Address = ", address)
except ValueError as e:
    print(e)
except:
    print("Error")
try:
    marks1 = int(input("Enter marks1 => "))
    marks2 = int(input("Enter marks2 => "))
    if marks1<0 or marks2<0:
        raise ValueError("Why u enter negative value")
    else:
        print("Total = ", marks1 + marks2)
except ValueError as e:
    print(e)
except:
    print("Error")
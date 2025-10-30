try:
    x=int(input("Enter no1 =>"))
    y=int(input("Enter no2 =>"))
    z=x/y
    print("Div =",z)
except ValueError:
    print("Why u enter string")
except ZeroDivisionError:
    print("Why u enter 0")
except:
    print("Other error")
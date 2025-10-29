buy = int(input("Enter buying price: "))
sell = int(input("Enter selling price: "))

if buy < sell:
    print("The User has made a profit.")
elif buy>sell:
    print("The User has made a loss.")
else:
    print("The User neither made a profit or loss")
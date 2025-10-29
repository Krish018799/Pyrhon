gender = input("Enter gender: ")
age = int(input("Enter age: "))

if age >= 18 and age < 30:
    if gender == "M":
        print("700 days")
    elif gender == "F":
        print("750 days")

elif age>= 30 and age<= 40:
     if gender == "M":
        print("800 days")
     elif gender == "F":
        print("850 days")
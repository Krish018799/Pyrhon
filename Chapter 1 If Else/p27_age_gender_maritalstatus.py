gender = input("Enter gender: ")
age = int(input("Enter age: "))
marital_status = input("Enter marital status: ")

if gender == "F":
    print("she will work only in urban areas.")
elif gender == "M":
    if age >= 20 and age <= 40:
        print("he may work anywhere.")
    elif age > 40 and age <= 60:
        print("he will work in urban areas only.")
    else:
        print("ERROR")
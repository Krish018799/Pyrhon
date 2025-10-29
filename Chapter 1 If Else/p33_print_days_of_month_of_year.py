year = int(input("Enter year=> "))
month = int(input("Enter month no=> "))

if month == 1:
    print("No. of days=> 31")
elif month == 2:
    if year%4 == 0:
        print("No. of days=> 29")
    else:
        print("No. of days=> 28")
elif month == 3:
    print("No. of days=> 31")
elif month == 4:
    print("No. of days=> 30")
elif month == 5:
    print("No. of days=> 31")
elif month == 6:
    print("No. of days=> 30")
elif month == 7:
    print("No. of days=> 31")
elif month == 8:
    print("No. of days=> 31")
elif month == 9:
    print("No. of days=> 30")
elif month == 10:
    print("No. of days=> 31")
elif month == 11:
    print("No. of days=> 30")
elif month == 12:
    print("No. of days=> 31")
else:
    print("Enter valid no.")
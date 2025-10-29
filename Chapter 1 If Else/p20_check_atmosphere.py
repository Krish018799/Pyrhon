temp = int(input("Enter temperature"))

if temp<=0:
    print("Freezing Atmosphere")
elif temp>0 and temp<=10:
    print("Very cold atmosphere")
elif temp>10 and temp<=20:
    print("Cold Atmosphere")
elif temp>20 and temp<=30:
    print("Normal Atmosphere")
elif temp>30 and temp<=40:
    print("Hot atmosphere")
elif temp>40:
    print("Very hot atmosphere")
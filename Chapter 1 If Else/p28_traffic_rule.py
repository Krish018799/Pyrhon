light = input("Enter color: ")

if light == "green":
    print("Car is allowed to go.")
elif light == "yellow":
    print("Car has to wait.")
elif light == "red":
    print("Car has to stop.")
else:
    print("Unrecognized signal")
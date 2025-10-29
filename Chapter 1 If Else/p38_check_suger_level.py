suger_level = int(input("Enter suger level=> "))

if suger_level < 80:
    print("Low suger level")
elif suger_level >= 80 and suger_level < 100:
    print("Normal suger level")
elif suger_level > 10:
    print("High suger level")
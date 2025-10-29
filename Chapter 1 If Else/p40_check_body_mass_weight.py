bmi = float(input("Enter BMI(body mass weight)=> "))

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("normal")
elif bmi >= 25 and bmi < 29.9:
    print("overweight")
elif bmi >= 30:
    print("obese")
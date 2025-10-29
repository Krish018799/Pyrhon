hindi = float(input("Enter marks of Hindi => "))
eng = float(input("Enter marks of English => "))
ss = float(input("Enter marks of English => "))

total = hindi + eng + ss

if total > 50:
    print("Your total is ", total, ". You are Pass")
else:
    print("Your total is ", total, ". You are Fail")
hindi = float(input("Enter marks of Hindi => "))
eng = float(input("Enter marks of English => "))
ss = float(input("Enter marks of English => "))

total = hindi + eng + ss

if total > 0 and total < 50:
    print("Your total is ",total,". You got C grade")
elif total >= 50 and total < 100:
    print("Your total is ", total, ". You got B grade")
elif total >= 100:
    print("Your total is ", total, ". You got A grade")
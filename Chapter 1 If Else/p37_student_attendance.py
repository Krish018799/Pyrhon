total_class = float(input("Number of classes held=> "))
class_attend = int(input("Enter class attend=> "))

attendance = (class_attend / float(total_class)) * 100

if attendance < 75:
    print("You are not allow to sit in exam")
else:
    print("You are allow to sit in exam")
math=int(input("Enter math marks: "))
eng= int(input("Enter eng marks: "))
science=int(input("Enter science marks: "))

total = math + eng + science

if total>99:
    print("Party time")
else:
    print("Call your dad")
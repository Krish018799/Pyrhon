a = int(input("Enter no. a:"))
b = int(input("Enter no. b:"))
c = int(input("Enter no. c:"))

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("All are equal")
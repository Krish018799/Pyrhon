n=int(input("Enter limit =>"))
s=0

for i in range(0,n+1,10):
    print(i,end= " + ")
    s+=i

print("\nSum = ", s)
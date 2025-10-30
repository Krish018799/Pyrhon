# 5X4X3X2X1

n = int(input("Enter limit=> "))
s=0
for i in range(n, 0, -1):
    print(i, end="*")
    s+=i
print("\nSum = ", s)

# here 1 is i++ in c and -1 is like i-- and 0 means i>0
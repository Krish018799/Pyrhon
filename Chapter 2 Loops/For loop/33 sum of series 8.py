# -1+2-3+4-5

n = int(input("Enter limit=> "))
s1=0
s2=0

for i in range(1, n+1):
    if(i%2==0):
        print(" +", i, end="")
        s1+=i
    else:
        print(" -", i, end="")
        s2-=i

print("\nSum of even no's = ", s1)
print("\nSubtraction of odd no's = ", s2)
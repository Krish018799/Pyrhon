n=int(input("Enter limit =>"))
i=n
f=1
while i>=1:
    print(i,end=" X ")
    f=f*i
    i=i-1
print("\nFact = ",f)
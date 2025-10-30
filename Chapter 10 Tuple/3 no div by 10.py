t1=(11,44,30,29,45,11,20,32,10)
sum = 0
c = 0
for x in t1:
    if x%10 == 0:
        print(x,end=" ")
        sum+=x
        c+=1

print("\nCount = ", c)
print("Sum = ", sum)
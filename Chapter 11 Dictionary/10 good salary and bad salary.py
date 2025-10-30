import random
d1 = {}
c1 = 0
c2 = 0
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    emp=i
    salary=random.randint(10000,50000)
    d1[emp]=salary

print("Employee\tSalary")
print("*"*30)
for e,s in d1.items():
    if s >= 20000:
        print(e,"\t\t\t",s, "\tGood salary")
        c1+=1
    else:
        print(e, "\t\t\t", s, "\tImprove your salary")
        c2+=2

print("\nGood salary count:", c1)
print("Improve salary count:", c2)
import random
d1 = {}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    emp=i
    salary=random.randint(10000,50000)
    d1[emp]=salary

print("Employee\tSalary")
print("*"*30)
for e,s in d1.items():
    print(e,"\t\t\t",s)
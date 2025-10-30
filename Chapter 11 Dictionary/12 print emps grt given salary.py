import random
d1 = {}
c1 = 0
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    emp=i
    salary=random.randint(10000,50000)
    d1[emp]=salary

s1 = int(input("Enter minimum salary: "))
print("Employee\tSalary")
print("*"*30)
for e,s in d1.items():
    if s > s1:
        print(e, "\t\t\t", s)
        c1 += 1

print("No of employees with salary grt ",s1,": ",c1)
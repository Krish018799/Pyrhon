import random
d1 = {}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    no=i
    marks=random.randint(1,50)
    d1[no]=marks

print("No\t\tMarks")
for k,v in d1.items():
    print(k,"\t\t",v)
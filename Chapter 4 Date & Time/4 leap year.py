import time
current = time.localtime(time.time())

m=current.tm_mon
d=current.tm_mday
y=current.tm_year
print(d,"/",m,"/",y)

if y%4 == 0:
    print("This is leap year")
else:
    print("This is not leap year")
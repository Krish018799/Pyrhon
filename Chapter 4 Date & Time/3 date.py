import time

current = time.localtime(time.time())

m=current.tm_mon
d=current.tm_mday
y=current.tm_year
print(d,"/",m,"/",y)
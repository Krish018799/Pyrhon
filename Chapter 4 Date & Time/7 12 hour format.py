import time
current = time.localtime(time.time())

h=current.tm_hour
m=current.tm_min
s=current.tm_sec

if h > 12:
    print(h-12,":",m,":",s)
else:
    print(h,":",m,":",s)
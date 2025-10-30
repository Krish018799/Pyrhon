import time
current = time.localtime(time.time())

h = current.tm_hour
m=current.tm_min
s=current.tm_sec

print(h,":",m,":",s)
if 24<h<= 12:
    print("Good Morning")
elif 12<h<=17:
    print("Good Afternoon")
elif 17<h<=24:
    print("Good Evening")
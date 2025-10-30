import time
current = time.localtime(time.time())

h = current.tm_hour

if h > 24 and h <=12:
    print(h, "AM")
else:
    print(h, "PM")
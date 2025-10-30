import time

current = time.localtime(time.time())
# above two lines are campalsary for date and time you can change name of current

print("Year:", current.tm_year)
print("Month:", current.tm_mon)
print("Date:", current.tm_mday, current.tm_mon, current.tm_year)
print("Day:", current.tm_mday)
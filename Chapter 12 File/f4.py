f1 = open("abc", "r")
c = 0
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch == " ":
        c = c+1
print("Total spaces are ",c)
f1.close()
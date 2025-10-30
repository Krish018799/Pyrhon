f1=open("abc","r")
f2=open("megh2","w")
f3=open("megh3","w")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch.isupper():
        f2.write(ch)
    elif ch.islower():
        f3.write(ch)
f1.close()
f2.close()
f2.close()
print("Copied")